from django.contrib import admin

from .admin_site import uae_admin_site

from .models import (
    Service,
    QuoteRequest,
    SiteSettings,
    Project,
    Testimonial,
    MaintenancePackage,
    ServiceArea,
    FAQ,
    Blog,
)


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = (
        'name',
        'price',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'description',
        'meta_title',
        'meta_description',
    )

    list_editable = (
        'price',
        'is_active',
    )

    ordering = (
        'name',
    )

    fieldsets = (
        (
            'Service Information',
            {
                'fields': (
                    'name',
                    'slug',
                    'description',
                    'price',
                    'image',
                    'is_active',
                )
            }
        ),
        (
            'SEO Settings',
            {
                'fields': (
                    'meta_title',
                    'meta_description',
                ),
                'classes': ('collapse',),
            }
        ),
    )

class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'service',
        'phone',
        'estimated_aed',
        'urgency',
        'status',
        'dispatch_status',
        'technician',
        'created_at',
    )

    list_filter = (
        'urgency',
        'status',
        'dispatch_status',
        'created_at',
    )

    search_fields = (
        'name',
        'phone',
        'email',
        'service',
        'technician',
    )

    list_editable = (
        'estimated_aed',
        'urgency',
        'status',
        'dispatch_status',
        'technician',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )


class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'whatsapp', 'email', 'address')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description', 'category')


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')
    search_fields = ('name', 'review')


class MaintenancePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


class ServiceAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'is_active')
    list_filter = ('service', 'is_active')
    search_fields = ('question', 'answer')


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'excerpt', 'content')


# Register models with UAE Care custom admin site
uae_admin_site.register(Service, ServiceAdmin)
uae_admin_site.register(QuoteRequest, QuoteRequestAdmin)
uae_admin_site.register(SiteSettings, SiteSettingsAdmin)
uae_admin_site.register(Project, ProjectAdmin)
uae_admin_site.register(Testimonial, TestimonialAdmin)
uae_admin_site.register(MaintenancePackage, MaintenancePackageAdmin)
uae_admin_site.register(ServiceArea, ServiceAreaAdmin)
uae_admin_site.register(FAQ, FAQAdmin)
uae_admin_site.register(Blog, BlogAdmin)