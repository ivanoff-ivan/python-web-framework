from django.db.models import signals
from django.dispatch import receiver

from common_tools.web.models import Profile


@receiver(signals.pre_save, sender=Profile)
def profile_created(instance, **kwargs):
    print(f'Pre created: {instance}')


@receiver(signals.post_save, sender=Profile)
def profile_created(instance, **kwargs):
    print(f'Post created: {instance}')


@receiver(signals.pre_delete, sender=Profile)
def profile_to_be_deleted(instance, **kwargs):
    instance.is_deleted = True
