from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('courses/', views.courses, name='courses'),
    path('gallery/', views.gallery, name='gallery'),
    path('send_contact_whatsapp/', views.send_contact_whatsapp, name='send_contact_whatsapp'),
]
