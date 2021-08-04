from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile

def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            first_name = f'{user.username}_firstname',
            last_name = f'{user.username}_lastname',
            email = f'{user.username}@{user.username}.com',
        )


def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(create_profile, sender=User)
post_delete.connect(delete_user, sender=Profile)