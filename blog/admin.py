from django.contrib import admin
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditor5Widget())  # CKEditor for the admin form

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}  # Auto-generate slug from the title

admin.site.register(Post, PostAdmin)
