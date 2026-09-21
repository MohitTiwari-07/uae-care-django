from django.contrib import admin

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


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'service', 'created_at')
    list_filter = ('created_at', 'service')
    search_fields = ('name', 'phone', 'email', 'service')
    readonly_fields = ('created_at',)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'whatsapp', 'email', 'address')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description', 'category')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'is_active')
    list_filter = ('rating', 'is_active')
    search_fields = ('name', 'review')


@admin.register(MaintenancePackage)
class MaintenancePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


@admin.register(ServiceArea)
class ServiceAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'is_active')
    list_filter = ('service', 'is_active')
    search_fields = ('question', 'answer')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'excerpt', 'content')