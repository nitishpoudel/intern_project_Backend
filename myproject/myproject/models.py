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
    label = models.CharField(max_length=80)
    href = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.label} ({self.href})"


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
