from django.db import models
from users.models import User
from django.urls import reverse


class Univer(models.Model):
    name = models.CharField(max_length = 100, help_text = 'Univer name')
    rector = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="univer")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('univer-detail', args=[str(self.id)])


class Chair(models.Model):
    name = models.CharField(max_length = 100, help_text = 'Chair name')
    univer = models.ForeignKey(Univer, on_delete=models.CASCADE, null=True, related_name='univer_chairs')
    head_of_dep = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='chairs_hod')
    # teacher = models.ManyToManyField(User)

    def __str__(self):
        return '{0}. Заведующая кафедрой - {1} {2} {3}'.format(self.name, self.head_of_dep.first_name, self.head_of_dep.middle_name, self.head_of_dep.last_name)

    def get_absolute_url(self):
        return reverse('chair-detail', args=[str(self.id)])


class Specialization(models.Model):
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE, null=True, blank=True, related_name='specializations')
    name = models.CharField(max_length=10, help_text='Spec name')
    unique_cod = models.CharField(max_length=5)

    def __str__(self):
        return '{0}, {1}'.format(self.name, self.unique_cod)

    def get_absolute_url(self):
        return reverse('spec-detail', args=[str(self.id)])


class GroupSpec(models.Model):
    name = models.CharField(max_length = 100,  help_text = 'Group name', blank=True, null=True)
    spec = models.ForeignKey(Specialization, on_delete=models.PROTECT, related_name='group_specs', null = True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    student = models.ManyToManyField(User)

    def __str__(self):
        return self.name or "name"
