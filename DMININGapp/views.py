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

# def python(request):
#     return render(request, 'python.html')

# def dataanalysis(request):
#     return render(request, 'dataanalysis.html')

# def datascience(request):
#     return render(request, 'datascience.html')

# def powerbi(request):
#     return render(request, 'powerbi.html')



