from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from tweeter.models import Profile


@receiver(post_save, sender=User)
def create_profile_for_user(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
