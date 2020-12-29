from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import TextChoices
from django.contrib.auth.hashers import make_password, UNUSABLE_PASSWORD_PREFIX


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,password):
        user = self.create_user(
            password=password,
            username=username
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class RoleTypes(TextChoices):
    STUDENT = 's'
    TEACHER = 't'
    RECTOR = 'r'
    HEAD_OF_DEP = 'hod'


class User(AbstractBaseUser, PermissionsMixin):
    role = models.CharField(max_length=16, choices=RoleTypes.choices, default='s')
    username = models.CharField(max_length=20, unique=True, null = True)
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50,null=True)
    group = models.ForeignKey("univers.GroupSpec", on_delete=models.SET_NULL, null=True)
    chair = models.ForeignKey('univers.Chair', on_delete=models.SET_NULL, null=True, blank=True,related_name='users')
    last_name = models.CharField(max_length=50,null = True)
    photo = models.ImageField(null=False, blank = False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['last_name', 'first_name']

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    objects = CustomUserManager()
    def __str__(self):
        return '{0} {1} {2}'.format(self.first_name,self.middle_name,self.last_name)

