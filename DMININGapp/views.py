from .models import Carousel, Course, CourseModal, Testimonial, ContactInfo
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

def index(request):
    carousel_items = Carousel.objects.all()
    courses = Course.objects.all()
    modals = CourseModal.objects.all()
    testimonials = Testimonial.objects.all()
    contact = ContactInfo.objects.first()
    return render(request, 'index.html', {
        'carousel_items': carousel_items,
        'courses': courses,
        'modals': modals,
        'testimonials': testimonials,
        'contact': contact
    })

def about(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'about.html', {
        'testimonials': testimonials
    })

def services(request):
    return render(request, 'services.html')

def courses(request):
    courses = Course.objects.all()
    modals = CourseModal.objects.all()
    return render(request, 'courses.html', {
        "courses": courses
        , "modals": modals
    })

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    contact = ContactInfo.objects.first()
    return render(request, 'contact.html', {
        'contact': contact
    })

def send_contact_mail(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],  # your website's email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully.")
        except Exception as e:
            messages.error(request, "There was an error sending your message. Please try again later.")

        return redirect('contact')  # redirect back to the contact page or another page



