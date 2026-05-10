from django.contrib import admin
from .models import (
    BlogParagraphOverride,
    NavItem,
    Post,
    Property,
    PropertyParagraphOverride,
    SiteSettings,
    TeamMember,
    Testimonial,
    AboutTab,
    Feature,
    ContactMessage,
    WhyChooseFeature,
    WhyChooseSection,
)


# ── Posts ────────────────────────────────────────────────────────────────────

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display    = ("title", "slug", "author", "is_published", "published_at")
    search_fields   = ("title", "slug", "author")
    list_filter     = ("is_published", "published_at")
    ordering        = ("-published_at", "-created_at")
    readonly_fields = ("created_at",)
    fields = (
        "title", "slug", "excerpt", "content",
        "author", "cover_image", "is_published", "published_at",
    )


# ── Properties ───────────────────────────────────────────────────────────────

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display   = ("title", "city", "type", "status", "price", "beds", "baths", "featured", "updated_at")
    list_editable  = ("featured",)
    list_filter    = ("status", "type", "city", "featured")
    search_fields  = ("title", "city", "description")
    ordering       = ("-updated_at",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Basic Info", {
            "fields": ("title", "city", "type", "status", "price", "featured"),
        }),
        ("Specs", {
            "fields": ("beds", "baths", "sqft"),
        }),
        ("Media", {
            "description": (
                'Enter image URLs as a JSON list. '
                'Example: ["https://example.com/img1.jpg", "https://example.com/img2.jpg"]'
            ),
            "fields": ("images",),
        }),
        ("Amenities", {
            "description": 'Enter amenities as a JSON list. Example: ["Pool", "Gym", "Parking"]',
            "fields": ("amenities",),
        }),
        ("Description", {
            "fields": ("description",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )


# ── Navigation ───────────────────────────────────────────────────────────────

@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display  = ("label", "href", "section", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter   = ("section", "is_active")
    search_fields = ("label", "href")
    ordering      = ("section", "order", "id")
    fields        = ("label", "href", "section", "order", "is_active")


# ── Blog / Property overrides ────────────────────────────────────────────────

@admin.register(BlogParagraphOverride)
class BlogParagraphOverrideAdmin(admin.ModelAdmin):
    list_display  = ("slug",)
    search_fields = ("slug",)
    fields        = ("slug", "excerpt", "content")


@admin.register(PropertyParagraphOverride)
class PropertyParagraphOverrideAdmin(admin.ModelAdmin):
    list_display  = ("property_id",)
    search_fields = ("property_id",)
    fields        = ("property_id", "description")


# ── Site Settings (singleton) ────────────────────────────────────────────────

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("General", {
            "fields": ("site_name", "logo_url", "phone", "email", "address"),
        }),
        ("Hero (Homepage)", {
            "fields": ("hero_title", "hero_bg_image"),
        }),
        ("Social Links", {
            "fields": ("facebook_url", "twitter_url", "instagram_url", "linkedin_url"),
            "classes": ("collapse",),
        }),
        ("About Page – Banner", {
            "fields": ("about_banner_title",),
        }),
        ("About Page – Who We Are", {
            "fields": (
                "who_we_are_heading", "about_title",
                "about_description_1", "about_description_2",
                "about_main_image", "experience_years",
            ),
        }),
        ("About Page – Stats Counters", {
            "description": (
                'JSON list of stat objects. '
                'Example: [{"value": "12K+", "label": "Properties"}, '
                '{"value": "7.5K+", "label": "Happy Clients"}, '
                '{"value": "320+", "label": "Expert Agents"}, '
                '{"value": "98%", "label": "Satisfaction"}]'
            ),
            "fields": ("about_stats",),
        }),
        ("About Page – Checklist Items", {
            "description": (
                'JSON list of strings. '
                'Example: ["Verified Properties", "Expert Agents", '
                '"Transparent Pricing", "24/7 Support", "Legal Assistance", "Home Inspection"]'
            ),
            "fields": ("about_checklist",),
        }),
        ("About Page – Our Purpose Section", {
            "fields": ("purpose_section_heading", "purpose_section_subtitle"),
        }),
        ("About Page – What We Do Section", {
            "fields": ("services_section_heading", "services_section_subtitle"),
        }),
        ("About Page – Why Choose Us Section", {
            "fields": ("why_us_eyebrow", "why_us_heading", "why_us_image"),
        }),
        ("About Page – Our Agents Section", {
            "fields": ("agents_section_heading", "agents_section_subtitle"),
        }),
        ("About Page – Testimonials Section", {
            "fields": ("testimonials_section_heading", "testimonials_section_subtitle"),
        }),
        ("About Page – CTA Banner", {
            "fields": ("cta_heading", "cta_subtext", "cta_button_label"),
        }),
        # ── Footer ──────────────────────────────────────────────────
        ("Footer – Newsletter Strip", {
            "fields": ("footer_newsletter_heading", "footer_newsletter_button"),
        }),
        ("Footer – About Column", {
            "fields": ("footer_tagline",),
        }),
        ("Footer – Column Headings", {
            "fields": (
                "footer_quick_links_heading",
                "footer_properties_heading",
                "footer_contact_heading",
            ),
        }),
        ("Footer – Contact Column", {
            "fields": ("footer_office_hours",),
        }),
        ("Footer – Copyright", {
            "fields": ("footer_copyright_extra",),
        }),
        # ── Contact Page ─────────────────────────────────────────────
        ("Contact Page – Banner", {
            "fields": (
                "contact_banner_eyebrow",
                "contact_banner_heading",
                "contact_banner_subtitle",
                "contact_banner_bg",
            ),
        }),
        ("Contact Page – Info Cards", {
            "fields": (
                "contact_address_label",
                "contact_phone_label",
                "contact_email_label",
                "contact_hours_label",
                "contact_hours_value",
            ),
        }),
        ("Contact Page – Map", {
            "description": "Paste the src URL from a Google Maps embed iframe.",
            "fields": ("contact_map_embed_url",),
        }),
        ("Contact Page – Form", {
            "fields": (
                "contact_form_heading",
                "contact_form_subtext",
                "contact_form_name_label",
                "contact_form_email_label",
                "contact_form_phone_label",
                "contact_form_subject_label",
                "contact_form_message_label",
                "contact_form_button_label",
                "contact_form_success_msg",
                "contact_form_error_msg",
            ),
        }),
        # ── Properties Page ──────────────────────────────────────────
        ("Properties Page – Banner", {
            "fields": (
                "properties_banner_eyebrow",
                "properties_banner_heading",
                "properties_banner_subtitle",
                "properties_banner_bg",
            ),
        }),
        ("Properties Page – Filter Bar", {
            "fields": (
                "properties_filter_city_placeholder",
                "properties_filter_type_placeholder",
                "properties_filter_status_placeholder",
                "properties_filter_min_placeholder",
                "properties_filter_max_placeholder",
                "properties_filter_button_label",
                "properties_empty_heading",
                "properties_empty_subtext",
            ),
        }),
        # ── Property Detail Page ─────────────────────────────────────
        ("Property Detail Page – Labels", {
            "fields": (
                "property_detail_eyebrow",
                "property_detail_section_heading",
                "property_detail_amenities_heading",
            ),
        }),
        ("Property Detail Page – Buy Card", {
            "fields": (
                "property_buy_card_heading",
                "property_buy_card_subtext",
                "property_buy_button_label",
            ),
        }),
    )

    def has_add_permission(self, request):
        # Only one record should ever exist
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ── Team Members ─────────────────────────────────────────────────────────────

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display  = ("name", "role", "order")
    list_editable = ("order",)
    search_fields = ("name", "role")
    ordering      = ("order",)
    fields        = ("name", "role", "image_url", "facebook", "twitter", "linkedin", "instagram", "order")


# ── Testimonials ─────────────────────────────────────────────────────────────

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display  = ("name", "role", "rating", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter   = ("is_active", "rating")
    search_fields = ("name", "role", "text")
    ordering      = ("order",)
    fields        = ("name", "role", "text", "rating", "avatar_url", "order", "is_active")


# ── About Tabs (Our Purpose section) ─────────────────────────────────────────

@admin.register(AboutTab)
class AboutTabAdmin(admin.ModelAdmin):
    list_display  = ("label", "heading", "order")
    list_editable = ("order",)
    search_fields = ("label", "heading", "body")
    ordering      = ("order",)
    fields        = ("label", "heading", "body", "points", "image_url", "order")


# ── Features (What We Do / Why Choose Us / About) ────────────────────────────

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display  = ("title", "category", "icon_name", "order")
    list_editable = ("order",)
    list_filter   = ("category",)
    search_fields = ("title", "description")
    ordering      = ("category", "order")
    fields        = ("category", "icon_name", "title", "description", "count", "count_label", "order")


# ── Contact Messages (read-only inbox) ───────────────────────────────────────

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ("name", "email", "subject", "created_at")
    search_fields   = ("name", "email", "subject")
    ordering        = ("-created_at",)
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    fields          = ("name", "email", "subject", "message", "created_at")

    def has_add_permission(self, request):
        return False  # submitted by visitors only

    def has_change_permission(self, request, obj=None):
        return False  # read-only


# ── Why Choose Us ────────────────────────────────────────────────────────────

@admin.register(WhyChooseFeature)
class WhyChooseFeatureAdmin(admin.ModelAdmin):
    list_display  = ("title", "stat_number", "stat_label", "order", "is_active")
    list_editable = ("order", "is_active")
    ordering      = ("order",)
    fields        = ("icon", "title", "description", "stat_number", "stat_label", "order", "is_active")


@admin.register(WhyChooseSection)
class WhyChooseSectionAdmin(admin.ModelAdmin):
    list_display = ("heading", "eyebrow_text", "is_active")
    fields       = ("eyebrow_text", "heading", "is_active")
