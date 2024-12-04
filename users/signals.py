from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print(f"Signal activated for user: {instance.username}")  # Дебагирање
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    try:
        print(f"Saving profile for user: {instance.username}")
        instance.profile.save()
    except Exception as e:
        print(f"Error saving profile: {e}")
