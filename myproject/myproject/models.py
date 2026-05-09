from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, null=True, blank=True)
    excerpt = models.TextField(blank=True)
    content = RichTextField()
    author = models.CharField(max_length=120, default="Prime Estates Editorial")
    cover_image = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:200] or "post"
            candidate = base_slug
            suffix = 1
            while Post.objects.exclude(pk=self.pk).filter(slug=candidate).exists():
                suffix += 1
                candidate = f"{base_slug[:190]}-{suffix}"
            self.slug = candidate

        if self.is_published and self.published_at is None:
            self.published_at = timezone.now().date()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Property(models.Model):
    TYPE_CHOICES = [
        ("villa", "Villa"),
        ("apartment", "Apartment"),
        ("condo", "Condo"),
        ("townhome", "Townhome"),
    ]
    STATUS_CHOICES = [
        ("sale", "For Sale"),
        ("rent", "For Rent"),
    ]

    title = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    price = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    sqft = models.PositiveIntegerField()
    featured = models.BooleanField(default=False)
    images = models.JSONField(default=list, blank=True)
    amenities = models.JSONField(default=list, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class NavItem(models.Model):
    SECTION_CHOICES = [
        ("navbar",       "Navbar"),
        ("quick_links",  "Footer – Quick Links"),
        ("properties",   "Footer – Properties"),
    ]
    label     = models.CharField(max_length=80)
    href      = models.CharField(max_length=255)
    order     = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    section   = models.CharField(
        max_length=20, choices=SECTION_CHOICES, default="navbar",
        help_text="Which part of the site this link belongs to.",
    )

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"[{self.get_section_display()}] {self.label} ({self.href})"


class BlogParagraphOverride(models.Model):
    slug = models.SlugField(max_length=220, unique=True)
    excerpt = models.TextField(blank=True)
    content = RichTextField(blank=True)

    def __str__(self):
        return self.slug


class PropertyParagraphOverride(models.Model):
    property_id = models.CharField(max_length=64, unique=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.property_id
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100, default="Prime Estates")
    logo_url = models.URLField(blank=True, null=True)
    hero_title = models.CharField(max_length=255, default="WELCOME TO REALTOR")
    hero_bg_image = models.URLField(default="https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1920&q=80")
    phone = models.CharField(max_length=20, default="+01 123 456 78")
    email = models.EmailField(default="info@realtor.com")
    address = models.TextField(default="123 Real Estate Ave, Luxury City, ST 12345")
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    # ── About Page – Banner ──────────────────────────────────────────
    about_banner_title = models.CharField(
        max_length=100, default="About Us",
        help_text="Large heading shown on the About page banner."
    )

    # ── About Page – Who We Are section ─────────────────────────────
    who_we_are_heading = models.CharField(
        max_length=100, default="Who We Are",
        help_text="Section heading for the 'Who We Are' block."
    )
    about_title = models.CharField(max_length=255, default="We Are The Best Real Estate Company In The Region")
    about_description_1 = models.TextField(
        blank=True,
        default="With over 15 years of experience, Realtor has helped thousands of families find their perfect homes across the region.",
    )
    about_description_2 = models.TextField(
        blank=True,
        default="We believe property hunting should be exciting, not stressful. From your first inquiry to closing day, we provide personalized guidance every step of the way.",
    )
    about_main_image = models.URLField(default="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&q=80")
    experience_years = models.PositiveIntegerField(default=15)

    # Stats counters – JSON list of {value, label} objects
    about_stats = models.JSONField(
        default=list,
        blank=True,
        help_text='e.g. [{"value": "12K+", "label": "Properties"}, {"value": "7.5K+", "label": "Happy Clients"}]',
    )
    # Checklist items – JSON list of strings
    about_checklist = models.JSONField(
        default=list,
        blank=True,
        help_text='e.g. ["Verified Properties", "Expert Agents", "Transparent Pricing"]',
    )

    # ── About Page – Our Purpose (tabs) section ──────────────────────
    purpose_section_heading = models.CharField(
        max_length=100, default="Our Purpose",
        help_text="Heading for the tabbed 'Our Purpose' section."
    )
    purpose_section_subtitle = models.CharField(
        max_length=255, blank=True,
        default="Discover what drives us every single day.",
    )

    # ── About Page – What We Do (features) section ───────────────────
    services_section_heading = models.CharField(
        max_length=100, default="What We Do",
        help_text="Heading for the 'What We Do' features section."
    )
    services_section_subtitle = models.CharField(
        max_length=255, blank=True,
        default="Comprehensive real estate services tailored to your needs.",
    )

    # ── About Page – Why Choose Us section ───────────────────────────
    why_us_eyebrow = models.CharField(
        max_length=100, default="Why Choose Us",
        help_text="Small label above the 'Why Choose Us' heading."
    )
    why_us_heading = models.CharField(
        max_length=255, default="The Right Choice For All Your Real Estate Needs",
        help_text="Main heading for the 'Why Choose Us' section."
    )
    why_us_image = models.URLField(
        default="https://images.unsplash.com/photo-1582407947304-fd86f028f716?w=800&q=80",
        help_text="Image shown on the left side of the 'Why Choose Us' section."
    )

    # ── About Page – Our Agents section ──────────────────────────────
    agents_section_heading = models.CharField(
        max_length=100, default="Our Great Agents",
        help_text="Heading for the team/agents section."
    )
    agents_section_subtitle = models.CharField(
        max_length=255, blank=True,
        default="Meet the experienced professionals dedicated to finding your perfect property.",
    )

    # ── About Page – Testimonials section ────────────────────────────
    testimonials_section_heading = models.CharField(
        max_length=100, default="What Our Clients Say",
        help_text="Heading for the testimonials section."
    )
    testimonials_section_subtitle = models.CharField(
        max_length=255, blank=True,
        default="Real stories from real people who found their perfect homes with us.",
    )

    # ── About Page – CTA Banner ───────────────────────────────────────
    cta_heading = models.CharField(
        max_length=255, default="Do you want to sell your property?",
        help_text="Heading text for the green CTA banner."
    )
    cta_subtext = models.CharField(
        max_length=255, blank=True,
        default="Call us and list your property here. We'll find the right buyer for you quickly.",
        help_text="Subtitle text below the CTA heading."
    )
    cta_button_label = models.CharField(
        max_length=80, default="Just Contact Us",
        help_text="Label for the CTA button."
    )

    # ── Footer ───────────────────────────────────────────────────────
    footer_tagline = models.TextField(
        blank=True,
        default="Your trusted partner in finding the perfect property. We combine smart discovery tools with responsive support.",
        help_text="Short description shown under the logo in the footer.",
    )
    footer_newsletter_heading = models.CharField(
        max_length=150, default="Subscribe to our newsletter",
        help_text="Heading text in the newsletter strip at the top of the footer.",
    )
    footer_newsletter_button = models.CharField(
        max_length=50, default="Subscribe",
        help_text="Button label for the newsletter subscription.",
    )
    footer_quick_links_heading = models.CharField(
        max_length=80, default="Quick Links",
        help_text="Column heading for the Quick Links section.",
    )
    footer_properties_heading = models.CharField(
        max_length=80, default="Properties",
        help_text="Column heading for the Properties links section.",
    )
    footer_contact_heading = models.CharField(
        max_length=80, default="Contact",
        help_text="Column heading for the Contact info section.",
    )
    footer_office_hours = models.CharField(
        max_length=100, default="Mon-Fri: 9:00 - 18:00",
        help_text="Office hours line shown in the footer contact column.",
    )
    footer_copyright_extra = models.CharField(
        max_length=100, blank=True, default="All rights reserved",
        help_text="Text after the year and site name in the copyright line.",
    )

    # ── Contact Page ─────────────────────────────────────────────────
    contact_banner_eyebrow = models.CharField(
        max_length=100, default="Get In Touch",
        help_text="Small label above the heading on the Contact page banner.",
    )
    contact_banner_heading = models.CharField(
        max_length=150, default="Contact Us",
        help_text="Main heading on the Contact page banner.",
    )
    contact_banner_subtitle = models.CharField(
        max_length=255, blank=True,
        default="Send your details and message. We will get back to you shortly.",
        help_text="Subtitle text below the heading on the Contact page banner.",
    )
    contact_banner_bg = models.URLField(
        blank=True, default="",
        help_text="Background image URL for the Contact page banner. Leave blank to use the default dark colour.",
    )
    # Info cards
    contact_address_label = models.CharField(max_length=80, default="Our Office", help_text="Label for the address card.")
    contact_phone_label   = models.CharField(max_length=80, default="Phone Number", help_text="Label for the phone card.")
    contact_email_label   = models.CharField(max_length=80, default="Email Address", help_text="Label for the email card.")
    contact_hours_label   = models.CharField(max_length=80, default="Working Hours", help_text="Label for the hours card.")
    contact_hours_value   = models.CharField(
        max_length=150, default="Mon – Fri: 9:00 AM – 6:00 PM",
        help_text="Working hours text shown in the hours card.",
    )
    # Map
    contact_map_embed_url = models.URLField(
        blank=True, default="",
        help_text=(
            "Google Maps embed URL. "
            "Go to Google Maps → Share → Embed a map → copy the src URL."
        ),
    )
    # Form texts
    contact_form_heading       = models.CharField(max_length=150, default="Send Us a Message", help_text="Heading inside the contact form card.")
    contact_form_subtext       = models.CharField(max_length=255, blank=True, default="Fill in the form below and our team will get back to you within 24 hours.", help_text="Subtitle inside the contact form card.")
    contact_form_name_label    = models.CharField(max_length=80, default="Full Name",     help_text="Label for the Name field.")
    contact_form_email_label   = models.CharField(max_length=80, default="Email Address", help_text="Label for the Email field.")
    contact_form_phone_label   = models.CharField(max_length=80, default="Phone Number",  help_text="Label for the Phone field.")
    contact_form_subject_label = models.CharField(max_length=80, default="Subject",       help_text="Label for the Subject field.")
    contact_form_message_label = models.CharField(max_length=80, default="Your Message",  help_text="Label for the Message field.")
    contact_form_button_label  = models.CharField(max_length=80, default="Send Message",  help_text="Submit button label.")
    contact_form_success_msg   = models.CharField(max_length=255, default="Thank you! Your message has been sent. We will get back to you shortly.", help_text="Message shown after successful form submission.")
    contact_form_error_msg     = models.CharField(max_length=255, default="Something went wrong. Please try again or contact us directly.", help_text="Message shown when form submission fails.")

    class Meta:
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image_url = models.URLField()
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    avatar_url = models.URLField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(
        default=True,
        help_text="Uncheck to hide this testimonial from the website without deleting it.",
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class AboutTab(models.Model):
    label = models.CharField(max_length=50)
    heading = models.CharField(max_length=255)
    body = models.TextField()
    points = models.JSONField(default=list)  # List of strings
    image_url = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.label


class Feature(models.Model):
    CATEGORY_CHOICES = [
        ("about", "About Us"),
        ("why_us", "Why Choose Us"),
        ("services", "What We Do"),
    ]
    icon_name = models.CharField(max_length=50)  # e.g., 'Home', 'Shield'
    title = models.CharField(max_length=100)
    description = models.TextField()
    count = models.CharField(max_length=50, blank=True, null=True)  # e.g., '2,500+'
    count_label = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'Properties Listed'
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.name} - {self.subject}"
class WhyChooseFeature(models.Model):
    ICON_CHOICES = [
        ('shield', 'Shield'),
        ('users', 'Users / Agents'),
        ('clock', 'Clock / Time'),
        ('home', 'Home'),
        ('star', 'Star'),
        ('check', 'Check'),
    ]

    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='shield')
    title = models.CharField(max_length=100)
    description = models.TextField()
    stat_number = models.CharField(max_length=20, help_text="e.g. 2,500+")
    stat_label = models.CharField(max_length=50, help_text="e.g. PROPERTIES LISTED")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Why Choose Feature"
        verbose_name_plural = "Why Choose Features"

    def __str__(self):
        return self.title


class WhyChooseSection(models.Model):
    """Controls the heading/subheading of the section"""
    eyebrow_text = models.CharField(max_length=100, default="WHY CHOOSE US")
    heading = models.CharField(max_length=200, default="Why Choose Prime Estates?")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Why Choose Section Header"

    def __str__(self):
        return self.heading
