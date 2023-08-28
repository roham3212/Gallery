from django.urls import path
from .views import *


app_name = 'root'
urlpatterns = [
    path('', home, name= 'home'),
    path('services', services, name= 'services'),
    path('gallery_single', gallery_single, name= 'gallery-single'),
    path('gallery', gallery, name= 'gallery'),
    path('contact', contact, name= 'contact'),
    path('about', about, name= 'about'),
]
