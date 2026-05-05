from rest_framework import serializers
from .models import (
    BlogParagraphOverride,
    NavItem,
    Post,
    Property,
    PropertyParagraphOverride,
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