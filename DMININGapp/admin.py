from django.contrib import admin
from .models import Carousel, Course, CourseModal, Testimonial, ContactInfo, GalleryImage

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'animation_direction')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "rating")

admin.site.register(CourseModal)
admin.site.register(Testimonial)
admin.site.register(ContactInfo)

admin.site.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')