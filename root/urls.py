from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('services', services),
    path('gallery_single', gallery_single),
    path('gallery', gallery),
    path('contact', contact),
    path('about', about),
]
