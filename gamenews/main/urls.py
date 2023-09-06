from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('properties', views.properties, name='properties'),
    path('contact', views.contact, name='contact'),
    path('propertyds', views.propertyds, name='propertyds')
]