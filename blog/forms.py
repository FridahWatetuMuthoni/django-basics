from .models import Post
from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms



class PostForm(ModelForm):
    body = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = Post
        fields = ['title','image','body','tags','slug']

class PostDeleteForm(ModelForm):
    class Meta:
        model = Post
        fields = []
