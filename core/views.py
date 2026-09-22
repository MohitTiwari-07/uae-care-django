from django.shortcuts import render, redirect
# import resend

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
        send_quote_email(quote)

        settings = SiteSettings.objects.first()

#         send_mail(
#             subject=f'New Quote Request - {service}',
#             message=f"""
# New Quote Request

# Name: {name}
# Phone: {phone}
# Email: {email}
# Service: {service}

# Message:
# {message}
# """,
#             from_email=None,
#             recipient_list=[settings.email],
#             fail_silently=False,
#         )

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
    services = Service.objects.filter(is_active=True)
    settings = SiteSettings.objects.first()

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
        send_quote_email(quote)

#         send_mail(
#             subject=f'New Quote Request - {service}',
#             message=f"""
# New Quote Request

# Name: {name}
# Phone: {phone}
# Email: {email}
# Service: {service}

# Message:
# {message}
# """,
#             from_email=None,
#             recipient_list=[settings.email],
#             fail_silently=True,
#         )

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


import json
import urllib.request
import urllib.error


def send_quote_email(quote):
    """
    Send quote email through Resend.
    Email failure will NEVER break the quote form.
    """

    try:
        api_key = getattr(settings, 'RESEND_API_KEY', None)

        if not api_key:
            print("RESEND_API_KEY is missing")
            return

        site_settings = SiteSettings.objects.first()

        if not site_settings or not site_settings.email:
            print("SiteSettings email is missing")
            return

        data = {
            "from": "UAE Care <onboarding@resend.dev>",
            "to": [site_settings.email],
            "subject": f"New Quote Request - {quote.service}",
            "html": f"""
                <h2>New Quote Request</h2>

                <p><strong>Name:</strong> {quote.name}</p>
                <p><strong>Phone:</strong> {quote.phone}</p>
                <p><strong>Email:</strong> {quote.email}</p>
                <p><strong>Service:</strong> {quote.service}</p>
                <p><strong>Message:</strong> {quote.message}</p>
            """
        }

        request = urllib.request.Request(
            "https://api.resend.com/emails",
            data=json.dumps(data).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST"
        )

        with urllib.request.urlopen(request, timeout=8) as response:
            result = response.read().decode("utf-8")
            print("Resend email response:", result)

    except Exception as e:
        print("RESEND EMAIL ERROR:", str(e))
        # IMPORTANT:
        # Never raise the error.
        # Quote is already saved in database.
        return

    
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def send_quote_email(quote):
    try:
        if not settings.RESEND_API_KEY:
            return

        resend.api_key = settings.RESEND_API_KEY

        site_settings = SiteSettings.objects.first()

        recipient = site_settings.email if site_settings else None

        if not recipient:
            return

        resend.Emails.send({
            "from": "UAE Care <onboarding@resend.dev>",
            "to": [recipient],
            "subject": f"New Quote Request - {quote.service}",
            "html": f"""
                <h2>New Quote Request</h2>

                <p><strong>Name:</strong> {quote.name}</p>
                <p><strong>Phone:</strong> {quote.phone}</p>
                <p><strong>Email:</strong> {quote.email}</p>
                <p><strong>Service:</strong> {quote.service}</p>
                <p><strong>Message:</strong> {quote.message}</p>
            """
        })

    except Exception as e:
        print("Resend email error:", e)

def send_quote_email(quote):
    try:
        if not settings.RESEND_API_KEY:
            print("RESEND_API_KEY not configured")
            return

        resend.api_key = settings.RESEND_API_KEY

        site_settings = SiteSettings.objects.first()

        if not site_settings or not site_settings.email:
            print("Recipient email not configured")
            return

        resend.Emails.send({
            "from": "UAE Care <onboarding@resend.dev>",
            "to": [site_settings.email],
            "subject": f"New Quote Request - {quote.service}",
            "html": f"""
                <h2>New Quote Request</h2>

                <p><strong>Name:</strong> {quote.name}</p>
                <p><strong>Phone:</strong> {quote.phone}</p>
                <p><strong>Email:</strong> {quote.email}</p>
                <p><strong>Service:</strong> {quote.service}</p>
                <p><strong>Message:</strong> {quote.message}</p>
            """
        })

        print("Quote email sent successfully")

    except Exception as e:
        print("Resend email error:", e)