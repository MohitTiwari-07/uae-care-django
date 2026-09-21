from django.contrib.admin import AdminSite
from .models import (
    Service,
    QuoteRequest,
    Project,
    Blog,
    SiteSettings,
)


class UAECareAdminSite(AdminSite):

    site_header = "UAE Care Admin CMS"
    site_title = "UAE Care"
    index_title = ""

    def index(self, request, extra_context=None):

        extra_context = extra_context or {}

        extra_context.update({
            "quote_count": QuoteRequest.objects.count(),

            "service_count": Service.objects.filter(
                is_active=True
            ).count(),

            "project_count": Project.objects.filter(
                is_active=True
            ).count(),

            "blog_count": Blog.objects.filter(
                is_active=True
            ).count(),

            "recent_quotes": QuoteRequest.objects.order_by(
                "-created_at"
            )[:5],

            "settings": SiteSettings.objects.first(),
        })

        return super().index(
            request,
            extra_context=extra_context
        )


uae_admin_site = UAECareAdminSite(name="uae_admin")