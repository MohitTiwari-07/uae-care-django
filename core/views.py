from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse

from decimal import Decimal
import json
import urllib.request

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


# =========================================================
# HOME
# =========================================================

def home(request):

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        # -------------------------------------------------
        # Get service price from Admin
        # -------------------------------------------------

        service_obj = Service.objects.filter(
            name=service,
            is_active=True
        ).first()

        estimated_aed = (
            service_obj.price
            if service_obj and service_obj.price is not None
            else Decimal("0")
        )

        # -------------------------------------------------
        # Save lead
        # -------------------------------------------------

        quote = QuoteRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            service=service,
            message=message,
            estimated_aed=estimated_aed
        )

        # -------------------------------------------------
        # Send email
        # -------------------------------------------------

        send_quote_email(quote)

        # -------------------------------------------------
        # Success message
        # -------------------------------------------------

        messages.success(
            request,
            'Thank you! Your quote request has been submitted successfully.'
        )

        return redirect('home')

    # -----------------------------------------------------
    # Homepage data
    # -----------------------------------------------------

    services = Service.objects.filter(is_active=True)
    site_settings = SiteSettings.objects.first()
    projects = Project.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    packages = MaintenancePackage.objects.filter(is_active=True)
    service_areas = ServiceArea.objects.filter(is_active=True)
    faqs = FAQ.objects.filter(is_active=True)
    blogs = Blog.objects.filter(is_active=True)

    return render(request, 'home.html', {
        'services': services,
        'settings': site_settings,
        'projects': projects,
        'testimonials': testimonials,
        'packages': packages,
        'service_areas': service_areas,
        'faqs': faqs,
        'blogs': blogs
    })


# =========================================================
# SERVICES
# =========================================================

def services(request):

    services = Service.objects.filter(
        is_active=True
    ).order_by('name')

    site_settings = SiteSettings.objects.first()

    return render(request, 'services.html', {
        'services': services,
        'settings': site_settings,
    })


# =========================================================
# PROJECTS
# =========================================================

def projects(request):

    site_settings = SiteSettings.objects.first()
    projects = Project.objects.filter(is_active=True)

    return render(request, 'projects.html', {
        'settings': site_settings,
        'projects': projects
    })


# =========================================================
# REVIEWS
# =========================================================

def reviews(request):

    site_settings = SiteSettings.objects.first()
    testimonials = Testimonial.objects.filter(is_active=True)

    return render(request, 'reviews.html', {
        'settings': site_settings,
        'testimonials': testimonials
    })


# =========================================================
# MAINTENANCE PACKAGES
# =========================================================

def maintenance_packages(request):

    site_settings = SiteSettings.objects.first()
    packages = MaintenancePackage.objects.filter(is_active=True)

    return render(request, 'maintenance_packages.html', {
        'settings': site_settings,
        'packages': packages
    })


# =========================================================
# ABOUT
# =========================================================

def about(request):

    site_settings = SiteSettings.objects.first()

    return render(request, 'about.html', {
        'settings': site_settings
    })


# =========================================================
# CONTACT
# =========================================================

def contact(request):

    site_settings = SiteSettings.objects.first()

    return render(request, 'contact.html', {
        'settings': site_settings
    })


# =========================================================
# REQUEST QUOTE
# =========================================================

def request_quote(request):

    services = Service.objects.filter(
        is_active=True
    ).order_by('name')

    site_settings = SiteSettings.objects.first()

    if request.method == 'POST':

        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()
        service = request.POST.get('service', '').strip()
        message = request.POST.get('message', '').strip()

        # -------------------------------------------------
        # Get service price from Admin
        # -------------------------------------------------

        service_obj = Service.objects.filter(
            name=service,
            is_active=True
        ).first()

        estimated_aed = (
            service_obj.price
            if service_obj and service_obj.price is not None
            else Decimal("0")
        )

        # -------------------------------------------------
        # Save quote request
        # -------------------------------------------------

        quote = QuoteRequest.objects.create(
            name=name,
            phone=phone,
            email=email,
            service=service,
            message=message,
            estimated_aed=estimated_aed
        )

        # -------------------------------------------------
        # Send email
        # -------------------------------------------------

        send_quote_email(quote)

        # -------------------------------------------------
        # Success message
        # -------------------------------------------------

        messages.success(
            request,
            'Thank you! Your quote request has been submitted successfully.'
        )

        return redirect('request_quote')

    return render(request, 'request_quote.html', {
        'settings': site_settings,
        'services': services
    })


# =========================================================
# SERVICE DETAIL
# =========================================================

def service_detail(request, slug):

    service = get_object_or_404(
        Service,
        slug=slug
    )

    site_settings = SiteSettings.objects.first()

    services = Service.objects.filter(
        is_active=True
    )

    faqs = FAQ.objects.filter(
        service=service,
        is_active=True
    )

    return render(request, 'service_detail.html', {
        'service': service,
        'settings': site_settings,
        'services': services,
        'faqs': faqs
    })


# =========================================================
# OLD SERVICE URL
# =========================================================

def old_service_detail(request, id):

    service = get_object_or_404(
        Service,
        id=id
    )

    return redirect(
        'service_detail',
        slug=service.slug
    )


# =========================================================
# BLOG DETAIL
# =========================================================

def blog_detail(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug
    )

    site_settings = SiteSettings.objects.first()

    return render(request, 'blog_detail.html', {
        'blog': blog,
        'settings': site_settings
    })


# =========================================================
# ROBOTS.TXT
# =========================================================

def robots_txt(request):

    content = """User-agent: *
Allow: /

Sitemap: https://uae-care-django.onrender.com/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )


# =========================================================
# SERVICE AREAS
# =========================================================

def service_areas(request):

    areas = ServiceArea.objects.filter(
        is_active=True
    ).order_by('name')

    site_settings = SiteSettings.objects.first()

    return render(
        request,
        'service_areas.html',
        {
            'areas': areas,
            'settings': site_settings,
        }
    )


# =========================================================
# SERVICE AREA DETAIL
# =========================================================

def service_area_detail(request, slug):

    area = get_object_or_404(
        ServiceArea,
        slug=slug,
        is_active=True
    )

    site_settings = SiteSettings.objects.first()

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
            'settings': site_settings,
            'services': services,
            'other_areas': other_areas,
        }
    )


# =========================================================
# BLOG
# =========================================================

def blog(request):

    site_settings = SiteSettings.objects.first()
    blogs = Blog.objects.filter(is_active=True)

    return render(request, 'blog.html', {
        'settings': site_settings,
        'blogs': blogs
    })


# =========================================================
# FAQS
# =========================================================

def faqs(request):

    site_settings = SiteSettings.objects.first()

    faq_list = FAQ.objects.filter(
        is_active=True
    )

    return render(request, 'faqs.html', {
        'settings': site_settings,
        'faqs': faq_list
    })


# =========================================================
# GOOGLE VERIFICATION
# =========================================================

def google_verification(request):

    file_path = settings.BASE_DIR / "googleb71cd020e600215b.html"

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        content = file.read()

    return HttpResponse(
        content,
        content_type="text/html"
    )


# =========================================================
# CUSTOM 404
# =========================================================

def custom_404(request, exception):

    return render(
        request,
        '404.html',
        status=404
    )


# =========================================================
# RESEND EMAIL
# =========================================================

def send_quote_email(quote):

    try:

        # -------------------------------------------------
        # Get Resend API key
        # -------------------------------------------------

        api_key = getattr(
            settings,
            'RESEND_API_KEY',
            None
        )

        if not api_key:

            print(
                "RESEND ERROR: RESEND_API_KEY is missing"
            )

            return

        # -------------------------------------------------
        # Get recipient email from admin settings
        # -------------------------------------------------

        site_settings = SiteSettings.objects.first()

        if not site_settings:

            print(
                "RESEND ERROR: SiteSettings not found"
            )

            return

        recipient = site_settings.email

        if not recipient:

            print(
                "RESEND ERROR: SiteSettings email is empty"
            )

            return

        # -------------------------------------------------
        # Email data
        # -------------------------------------------------

        data = {

            # IMPORTANT:
            # Replace this after your Resend domain
            # is verified.
            "from": "UAE Care <onboarding@resend.dev>",

            "to": [
                recipient
            ],

            "subject": (
                f"New Quote Request - {quote.service}"
            ),

            "html": f"""
                <div style="
                    font-family: Arial, sans-serif;
                    max-width: 650px;
                    margin: auto;
                    padding: 25px;
                    border: 1px solid #ddd;
                    border-radius: 10px;
                ">

                    <h2>
                        New Quote Request
                    </h2>

                    <hr>

                    <p>
                        <strong>Name:</strong>
                        {quote.name}
                    </p>

                    <p>
                        <strong>Phone:</strong>
                        {quote.phone}
                    </p>

                    <p>
                        <strong>Email:</strong>
                        {quote.email}
                    </p>

                    <p>
                        <strong>Service:</strong>
                        {quote.service}
                    </p>

                    <p>
                        <strong>Estimated AED:</strong>
                        AED {quote.estimated_aed}
                    </p>

                    <p>
                        <strong>Message:</strong>
                    </p>

                    <p>
                        {quote.message}
                    </p>

                    <hr>

                    <p>
                        UAE Care Website
                    </p>

                </div>
            """
        }

        # -------------------------------------------------
        # Resend API request
        # -------------------------------------------------

        api_request = urllib.request.Request(

            "https://api.resend.com/emails",

            data=json.dumps(
                data
            ).encode("utf-8"),

            headers={

                "Authorization":
                    f"Bearer {api_key}",

                "Content-Type":
                    "application/json",

            },

            method="POST"
        )

        # -------------------------------------------------
        # Send email
        # -------------------------------------------------

        with urllib.request.urlopen(
            api_request,
            timeout=8
        ) as response:

            result = response.read().decode(
                "utf-8"
            )

            print(
                "RESEND SUCCESS:",
                result
            )

    except Exception as e:

        # IMPORTANT:
        # Email failure must never
        # break the quote form.

        print(
            "RESEND EMAIL ERROR:",
            repr(e)
        )

        return