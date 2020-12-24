from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.contrib import admin
from users.models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','role','first_name','middle_name','last_name','photo', 'is_active')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    Model = User
    fields = ('last_name',)

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'role')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active',)}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(UserAdmin, self).get_fieldsets(request, obj)
        if obj is None:
            return fieldsets
        print(obj.role)
        if obj.role == 's':
            fieldsets[0][1]['fields']=('first_name','password', 'middle_name', 'last_name','group')
        if obj.role == 'hod':
            fieldsets[0][1]['fields']=('first_name', 'password','middle_name', 'last_name','is_hod')
        if obj.role == 'r':
            fieldsets[0][1]['fields']=('first_name','password', 'middle_name', 'last_name','is_rector',)
        return fieldsets

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2','role','first_name','middle_name','last_name','photo', 'is_active')}
        ),
    )


admin.site.register(User, UserAdmin)