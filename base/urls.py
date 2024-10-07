from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('blog/', include('blog.urls')),
    path('users/',include('users.urls')),
    path('accounts/', include('allauth.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
