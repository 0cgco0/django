"""
URL configuration for cleangrave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.conf import settings

urlpatterns = [

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.home, name='home'),
    path('how-it-works/', views.howitworks, name="how-it-works"),
    path('blog/', views.blog, name="blog"),
    path('blog/1/', views.blog1, name="blog1"),
    path('blog/2/', views.blog2, name="blog2"),
    path('blog/3/', views.blog3, name="blog3"),
    path('locations/', views.locations, name="locations"),
    path('terms/', views.terms, name="terms"),
    path('privacy/', views.privacy, name="privacy"),
    path('contact/', views.contact, name="contact"),
    path('admin/', admin.site.urls),
   
]
urlpatterns += staticfiles_urlpatterns()