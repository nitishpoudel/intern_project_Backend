from rest_framework import serializers
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

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = "__all__"


class NavItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavItem
        fields = "__all__"


class BlogParagraphOverrideSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogParagraphOverride
        fields = "__all__"


class PropertyParagraphOverrideSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyParagraphOverride
        fields = "__all__"


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class AboutTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTab
        fields = "__all__"


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"


class WhyChooseFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseFeature
        fields = "__all__"


class WhyChooseSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseSection
        fields = "__all__"