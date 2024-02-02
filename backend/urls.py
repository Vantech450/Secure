from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import settings

urlpatterns = [
    path('Vatrent/', admin.site.urls),
    path('', include('base.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]

if settings.DEBUG: