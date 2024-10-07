from django.db import models
from django.contrib.auth.models import AbstractUser
from pilkit.processors import ResizeToFill
from imagekit.models import ImageSpecField

# Create your models here.

GENDER = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'),)


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profiles/', default='profiles/default.png')
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(
        max_length=200, choices=GENDER, null=True, blank=True)
    image_thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(150,150)], format='JPEG',options={'quality':60})

    
    def __str__(self):
        return self.email
