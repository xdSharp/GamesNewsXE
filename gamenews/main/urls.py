from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews', views.reviews, name='reviews'),
    path('guides', views.guides, name='guides'),
    path('contacts', views.contacts, name='contacts')
]