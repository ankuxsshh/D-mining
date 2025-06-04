from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/carousel/')
    animation_direction = models.CharField(
        max_length=10,
        choices=[('Left', 'fadeInLeft'), ('Right', 'fadeInRight')],
        default='Right'
    )

    def __str__(self):
        return self.title
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    rating = models.IntegerField(default=5)
    iimage = models.ImageField(upload_to='static/courses/', null=True, blank=True)
    short_description = models.TextField()
    delay = models.CharField(max_length=10, default=".3s")  # For animation delay
    modal_target = models.CharField(max_length=50, default="#")  # e.g., "#modalPython"

    def __str__(self):
        return self.title
    

class CourseModal(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    exercises = models.PositiveIntegerField()
    duration = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    learners = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/modals/')
    modal_id = models.CharField(max_length=100, help_text="E.g. modalPython, modalPowerBI")

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)  # e.g., 'B.Tech Final Year'
    feedback = models.TextField()
    image = models.ImageField(upload_to='static/testimonials/')
    rating = models.PositiveSmallIntegerField(default=5)  # from 1 to 5 stars

    def __str__(self):
        return self.name
    
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    address_link = models.URLField(help_text="Google Maps embed link")
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "Contact Information"
