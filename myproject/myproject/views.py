from rest_framework.response import Response
from rest_framework.views import APIView
from .models import (
    BlogParagraphOverride,
    NavItem,
    Post,
    Property,
    PropertyParagraphOverride,
)
from .serializers import (
    BlogParagraphOverrideSerializer,
    NavItemSerializer,
    PostSerializer,
    PropertyParagraphOverrideSerializer,
    PropertySerializer,
)


class ApiRootView(APIView):
    def get(self, request):
        return Response(
            {
                "message": "Prime Estates API",
                "endpoints": [
                    "/api/properties/",
                    "/api/properties/<id>/",
                    "/api/nav-items/",
                    "/api/blog-posts/",
                    "/api/blog-posts/<slug>/",
                    "/api/blog-paragraph-overrides/",
                    "/api/property-paragraph-overrides/",
                ],
            }
        )


class PropertyListView(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        prop_type = request.query_params.get("type")
        status = request.query_params.get("status")
        min_price = request.query_params.get("minPrice")
        max_price = request.query_params.get("maxPrice")
        featured = request.query_params.get("featured")

        filtered = Property.objects.all()

        if city:
            filtered = filtered.filter(city=city)
        if prop_type:
            filtered = filtered.filter(type=prop_type)
        if status:
            filtered = filtered.filter(status=status)

        if min_price:
            try:
                min_price_value = int(min_price)
                filtered = filtered.filter(price__gte=min_price_value)
            except ValueError:
                pass

        if max_price:
            try:
                max_price_value = int(max_price)
                filtered = filtered.filter(price__lte=max_price_value)
            except ValueError:
                pass
        if featured == "true":
            filtered = filtered.filter(featured=True)

        return Response(PropertySerializer(filtered, many=True).data)


class PropertyDetailView(APIView):
    def get(self, request, property_id):
        try:
            property_obj = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response({"detail": "Property not found"}, status=404)
        return Response(PropertySerializer(property_obj).data)


class NavItemListView(APIView):
    def get(self, request):
        items = NavItem.objects.filter(is_active=True)
        return Response(NavItemSerializer(items, many=True).data)


class BlogPostListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(is_published=True, slug__isnull=False).exclude(slug="").order_by("-published_at", "-created_at")
        limit = request.query_params.get("limit")
        if limit:
            try:
                posts = posts[: int(limit)]
            except ValueError:
                pass
        return Response(PostSerializer(posts, many=True).data)


class BlogPostDetailView(APIView):
    def get(self, request, slug):
        try:
            post = Post.objects.get(slug=slug, is_published=True)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found"}, status=404)
        return Response(PostSerializer(post).data)


class BlogParagraphOverrideListView(APIView):
    def get(self, request):
        records = BlogParagraphOverride.objects.all()
        return Response(BlogParagraphOverrideSerializer(records, many=True).data)


class PropertyParagraphOverrideListView(APIView):
    def get(self, request):
        records = PropertyParagraphOverride.objects.all()
        return Response(PropertyParagraphOverrideSerializer(records, many=True).data)