from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GroupSpec


@receiver(post_save, sender=GroupSpec)
def my_group(sender, instance, created, **kwargs):
    if created or instance.name is None:
        year = instance.start_date.year
        count = instance.spec.group_specs.filter(start_date__year=year).count()
        unique_cod = instance.spec.unique_cod
        instance.name = f"{unique_cod}-{str(year)[2:]}-{count+1}"
        instance.save()

