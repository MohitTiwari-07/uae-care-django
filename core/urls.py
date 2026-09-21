from django.urls import path
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemaps import ServiceSitemap, BlogSitemap


sitemaps = {
    'services': ServiceSitemap,
    'blogs': BlogSitemap,
}


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
path('request-quote/', views.request_quote, name='request_quote'),
path('projects/', views.projects, name='projects'),
path('reviews/', views.reviews, name='reviews'),
path('maintenance-packages/', views.maintenance_packages, name='maintenance_packages'),
path('blog/', views.blog, name='blog'),
path('faqs/', views.faqs, name='faqs'),

   path(
    'services/<slug:slug>/',
    views.service_detail,
    name='service_detail'
),
path(
    'services/id/<int:id>/',
    views.old_service_detail,
),

    path(
        'blog/<slug:slug>/',
        views.blog_detail,
        name='blog_detail'
    ),
    path('robots.txt', views.robots_txt, name='robots_txt'),    

    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django-sitemap'
    ),
    path(
    'service-areas/<slug:slug>/',
    views.service_area_detail,
    name='service_area_detail'
),
]