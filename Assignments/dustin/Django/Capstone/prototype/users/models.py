from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os

class Profile(models.Model):
    def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'users/{0}/{1}'.format(instance.user.username, filename)
    #email = models.EmailField(('email_address'), unique=True)
    is_anonymous = False
    is_authenticated = True
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # general
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    favorites = models.ManyToManyField('cc.ArtPiece', blank=True)
    
    # settings
    name = models.CharField(max_length = 32, null=True, blank=True)
    location = models.CharField(max_length = 64, null=True, blank=True)    
    bio = models.TextField(null=True, blank=True)    
    mediums = models.ManyToManyField('Medium', blank=True)
    misc = models.CharField(max_length = 1000, null=True, blank=True)
    theme = models.ForeignKey('Theme', on_delete=models.PROTECT, null=False, blank=True, default=1)
    layout = models.ForeignKey('Layout', on_delete=models.PROTECT, null=False, blank=True, default=1)
    #layout = models.ForeignKey('Layout', on_delete=models.PROTECT, null=False, blank=True, default=Layout.objects.get(text='Type 1').id)
    instagram = models.CharField(max_length = 150, null=True, blank=True)
    patreon = models.CharField(max_length = 150, null=True, blank=True)
    soundcloud = models.CharField(max_length = 150, null=True, blank=True)
    profile_pic = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    




class Theme(models.Model):
    text = models.CharField(max_length = 150)

    def __str__(self):
        return self.text

class Layout(models.Model):
    text = models.CharField(max_length = 150)

    def __str__(self):
        return self.text

class Medium(models.Model):
    text = models.CharField(max_length = 150)

    def __str__(self):
        return self.text
    
    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# Create your models here.
