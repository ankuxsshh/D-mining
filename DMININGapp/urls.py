from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('courses/', views.courses, name='courses'),
    # path('python/', views.python, name='python'),
    # path('dataanalysis/', views.dataanalysis, name='dataanalysis'),
    # path('datascience/', views.datascience, name='datascience'),
    # path('powerbi/', views.powerbi, name='powerbi'),
]
