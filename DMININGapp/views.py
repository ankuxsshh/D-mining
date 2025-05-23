from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def courses(request):
    return render(request, 'courses.html')

def gallery(request):
    return render(request, 'gallery.html')


