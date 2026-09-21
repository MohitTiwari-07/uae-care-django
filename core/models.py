from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    service = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    phone = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=255)

    def __str__(self):
        return "Website Settings"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class MaintenancePackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    features = models.TextField(
        help_text="Enter each feature on a new line"
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ServiceArea(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, null=True)

    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)

    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='faqs',
        null=True,
        blank=True
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    meta_title = models.CharField(max_length=200, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)

    excerpt = models.TextField()
    content = models.TextField()
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title