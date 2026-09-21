from django.contrib.sitemaps import Sitemap
from .models import Service, Blog


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Service.objects.filter(is_active=True)

    def location(self, obj):
        return f"/services/{obj.slug}/"


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Blog.objects.filter(is_active=True)

    def location(self, obj):
        return f"/blog/{obj.slug}/"