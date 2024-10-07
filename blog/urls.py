from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('blogs/', views.blogs, name='blogs'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('tags/<slug:tag>/', views.home, name='posts_by_tag'),

]
