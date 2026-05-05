from django.contrib import admin
from .models import (
    BlogParagraphOverride,
    NavItem,
    Post,
    Property,
    PropertyParagraphOverride,
)

class StaffEditableAdmin(admin.ModelAdmin):
    """
    Allow staff users to manage content models in Django admin
    even when granular model permissions are not assigned.
    """
    def _is_staff(self, request):
        return bool(request.user and request.user.is_active and request.user.is_staff)

    def has_module_permission(self, request):
        return self._is_staff(request)

    def has_view_permission(self, request, obj=None):
        return self._is_staff(request)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return self._is_staff(request)

    def has_delete_permission(self, request, obj=None):
        return False


class PostAdmin(StaffEditableAdmin):
    list_display = ("title", "slug", "author", "is_published", "published_at")
    search_fields = ("title", "slug", "author")
    list_filter = ("is_published", "published_at")
    ordering = ("-published_at", "-created_at")
    readonly_fields = ("created_at",)
    fields = (
        "title",
        "slug",
        "excerpt",
        "content",
        "author",
        "cover_image",
        "is_published",
        "published_at",
    )

    def has_add_permission(self, request):
        return self._is_staff(request)

    def has_delete_permission(self, request, obj=None):
        return self._is_staff(request)


class PropertyAdmin(StaffEditableAdmin):
    list_display = ("title", "city", "type", "status", "price", "featured", "updated_at")
    search_fields = ("title", "city")
    list_filter = ("status", "type", "city", "featured")
    ordering = ("-updated_at",)
    fields = ("description",)


class NavItemAdmin(StaffEditableAdmin):
    list_display = ("label", "href", "order", "is_active")
    search_fields = ("label", "href")
    list_filter = ("is_active",)
    ordering = ("order", "id")


class BlogParagraphOverrideAdmin(StaffEditableAdmin):
    list_display = ("slug",)
    search_fields = ("slug",)
    fields = ("slug", "excerpt", "content")

    def has_add_permission(self, request):
        return self._is_staff(request)

    def has_delete_permission(self, request, obj=None):
        return self._is_staff(request)


class PropertyParagraphOverrideAdmin(StaffEditableAdmin):
    list_display = ("property_id",)
    search_fields = ("property_id",)
    fields = ("description",)


admin.site.register(Post, PostAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(NavItem, NavItemAdmin)
admin.site.register(BlogParagraphOverride, BlogParagraphOverrideAdmin)
admin.site.register(PropertyParagraphOverride, PropertyParagraphOverrideAdmin)