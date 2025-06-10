from .models import Carousel, Course, CourseModal, Testimonial, ContactInfo, GalleryImage
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from urllib.parse import quote

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
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html'
                  , {
                      'images': images
                      })

def contact(request):
    contact = ContactInfo.objects.first()
    return render(request, 'contact.html', {
        'contact': contact
    })

def send_contact_whatsapp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        qualification = request.POST.get('qualification')
        message = request.POST.get('message')

        full_message = f"New Contact Message :\n\nName : {name}\nPhone : {phone}\nQualification : {qualification}\n\nMessage :\n{message}"

        # Replace with your WhatsApp number (include country code, no + sign)
        whatsapp_number = '916282922334'

        # Encode the message for the URL
        encoded_message = quote(full_message)

        # WhatsApp API redirect URL
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

        return redirect(whatsapp_url)



