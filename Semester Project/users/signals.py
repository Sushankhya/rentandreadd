import email
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.contrib.auth.models import User



def createProfile(sender, instance, created, **kwarg):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            email= user.email
        )

def profileDeleted(sender, instance, **kwarg):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(profileDeleted, sender=Profile)