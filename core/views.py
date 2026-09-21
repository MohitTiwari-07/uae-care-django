from django.shortcuts import render, redirect
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import (
    Service,
    QuoteRequest,
    SiteSettings,
    Project,
    Testimonial,
    MaintenancePackage,
    ServiceArea,
    FAQ,
    Blog
)


def home(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        QuoteRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            service=service,
            message=message
        )

        settings = SiteSettings.objects.first()

        send_mail(
            subject=f'New Quote Request - {service}',
            message=f"""
New Quote Request

Name: {name}
Phone: {phone}
Email: {email}
Service: {service}

Message:
{message}
""",
            from_email=None,
            recipient_list=[settings.email],
            fail_silently=False,
        )

        messages.success(
            request,
            'Thank you! Your quote request has been submitted successfully.'
        )

    services = Service.objects.filter(is_active=True)
    settings = SiteSettings.objects.first()
    projects = Project.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    packages = MaintenancePackage.objects.filter(is_active=True)
    service_areas = ServiceArea.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    blogs = Blog.objects.filter(is_active=True)

    return render(request, 'home.html', {
        'services': services,
        'settings': settings,
        'projects': projects,
        'testimonials': testimonials,
        'packages': packages,
        'service_areas': service_areas,
        'faqs': faqs,
        'blogs': blogs
    })

def services(request):
    services = Service.objects.filter(is_active=True).order_by('name')
    settings = SiteSettings.objects.first()

    return render(request, 'services.html', {
        'services': services,
        'settings': settings,
    })

def projects(request):
    settings = SiteSettings.objects.first()
    projects = Project.objects.filter(is_active=True)

    return render(request, 'projects.html', {
        'settings': settings,
        'projects': projects
    })


def reviews(request):
    settings = SiteSettings.objects.first()
    testimonials = Testimonial.objects.filter(is_active=True)

    return render(request, 'reviews.html', {
        'settings': settings,
        'testimonials': testimonials
    })


def maintenance_packages(request):
    settings = SiteSettings.objects.first()
    packages = MaintenancePackage.objects.filter(is_active=True)

    return render(request, 'maintenance_packages.html', {
        'settings': settings,
        'packages': packages
    })

def about(request):
    settings = SiteSettings.objects.first()

    return render(request, 'about.html', {
        'settings': settings
    })

def contact(request):
    settings = SiteSettings.objects.first()

    return render(request, 'contact.html', {
        'settings': settings
    })


def request_quote(request):
    settings = SiteSettings.objects.first()
    services = Service.objects.filter(is_active=True)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        if not name or not phone or not email or not service:
            messages.error(
                request,
                'Please fill in all required fields.'
            )
        else:
            QuoteRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service,
                message=message
            )

            # Email notification
            send_mail(
                subject=f'New Quote Request - {service}',
                message=f"""
New Quote Request

Name: {name}
Phone: {phone}
Email: {email}
Service: {service}

Message:
{message}
""",
                from_email=None,
                recipient_list=[settings.email],
                fail_silently=False,
            )

            messages.success(
                request,
                'Thank you! Your quote request has been submitted successfully.'
            )

            return redirect('request_quote')

    return render(request, 'request_quote.html', {
        'settings': settings,
        'services': services
    })


def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    settings = SiteSettings.objects.first()
    services = Service.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(
    service=service,
    is_active=True
)


    return render(request, 'service_detail.html', {
        'service': service,
        'settings': settings,
        'services': services,
        'faqs': faqs
    })
def old_service_detail(request, id):
    service = Service.objects.get(id=id)
    return redirect('service_detail', slug=service.slug)

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    settings = SiteSettings.objects.first()

    return render(request, 'blog_detail.html', {
        'blog': blog,
        'settings': settings
    })



from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
Allow: /

Sitemap: https://uae-care-django.onrender.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")

def service_areas(request):
    areas = ServiceArea.objects.filter(
        is_active=True
    ).order_by('name')

    settings = SiteSettings.objects.first()

    return render(
        request,
        'service_areas.html',
        {
            'areas': areas,
            'settings': settings,
        }
    )


def service_area_detail(request, slug):
    area = get_object_or_404(
        ServiceArea,
        slug=slug,
        is_active=True
    )

    settings = SiteSettings.objects.first()

    services = Service.objects.filter(
        is_active=True
    ).order_by('name')

    other_areas = ServiceArea.objects.filter(
        is_active=True
    ).exclude(
        id=area.id
    ).order_by('name')

    return render(
        request,
        'service_area_detail.html',
        {
            'area': area,
            'settings': settings,
            'services': services,
            'other_areas': other_areas,
        }
    )
def blog(request):
    settings = SiteSettings.objects.first()
    blogs = Blog.objects.filter(is_active=True)

    return render(request, 'blog.html', {
        'settings': settings,
        'blogs': blogs
    })


def faqs(request):
    settings = SiteSettings.objects.first()
    faq_list = FAQ.objects.filter(is_active=True)

    return render(request, 'faqs.html', {
        'settings': settings,
        'faqs': faq_list
    })

def google_verification(request):
    file_path = settings.BASE_DIR / "googleb71cd020e600215b.html"

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return HttpResponse(content, content_type="text/html")