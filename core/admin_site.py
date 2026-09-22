from django.contrib.admin import AdminSite
from django.db.models import Sum

from .models import (
    Service,
    QuoteRequest,
    Project,
    Blog,
    SiteSettings,
    MaintenancePackage,
)


class UAECareAdminSite(AdminSite):

    site_header = "UAE Care Admin CMS"
    site_title = "UAE Care"
    index_title = ""

    def index(self, request, extra_context=None):

        extra_context = extra_context or {}

        # Total leads
        total_leads = QuoteRequest.objects.count()

        # Pipeline value = all open leads' estimated value
        pipeline_value = (
            QuoteRequest.objects
            .exclude(status__in=["completed", "cancelled"])
            .aggregate(total=Sum("estimated_aed"))["total"] or 0
        )

        # Currently dispatched / on-site jobs
        active_dispatches = QuoteRequest.objects.filter(
            dispatch_status__in=["dispatched", "on_site"]
        ).count()

        # Active emergency 24/7 calls
        emergency_calls = QuoteRequest.objects.filter(
            urgency="emergency"
        ).exclude(
            status__in=["completed", "cancelled"]
        ).count()

        extra_context.update({
            "quote_count": total_leads,

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
            "maintenance_package": MaintenancePackage.objects.filter(
    is_active=True
).first(),

            # CRM KPI values
            "pipeline_value": pipeline_value,
            "active_dispatches": active_dispatches,
            "emergency_calls": emergency_calls,
        })

        return super().index(
            request,
            extra_context=extra_context
        )


uae_admin_site = UAECareAdminSite(name="uae_admin")