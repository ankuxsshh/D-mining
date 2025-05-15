from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DMININGapp.urls')),  # include the app's URL patterns
]
