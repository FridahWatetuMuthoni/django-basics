from django.db import models
from django.utils.text import slugify
from django.urls import reverse 
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager
from pilkit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.

User = get_user_model()


class Post(models.Model):
    title= models.CharField(max_length=250)
    image = models.ImageField(upload_to="blog/")
    body = CKEditor5Field('Text', config_name='extends')
    slug = models.SlugField(blank=True, default="", max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(1200,300)], format='JPEG',options={'quality':60})
    tags = TaggableManager()

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.slug)])
    
    
    def __str__(self):
        return self.title
