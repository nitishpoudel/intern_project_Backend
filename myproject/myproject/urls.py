"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from myproject.views import (
    ApiRootView,
    BlogParagraphOverrideListView,
    BlogPostDetailView,
    BlogPostListView,
    NavItemListView,
    PropertyParagraphOverrideListView,
    PropertyDetailView,
    PropertyListView,
    SiteSettingsView,
    TeamMemberListView,
    TestimonialListView,
    AboutTabListView,
    FeatureListView,
    ContactMessageCreateView,
    WhyChooseFeatureListView,
    WhyChooseSectionView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("api/", ApiRootView.as_view(), name="api-root"),
    path("api/properties/", PropertyListView.as_view(), name="property-list"),
    path("api/properties/<int:property_id>/", PropertyDetailView.as_view(), name="property-detail"),
    path("api/nav-items/", NavItemListView.as_view(), name="nav-item-list"),
    path("api/blog-posts/", BlogPostListView.as_view(), name="blog-post-list"),
    path("api/blog-posts/<slug:slug>/", BlogPostDetailView.as_view(), name="blog-post-detail"),
    path("api/blog-paragraph-overrides/", BlogParagraphOverrideListView.as_view(), name="blog-paragraph-override-list"),
    path("api/property-paragraph-overrides/", PropertyParagraphOverrideListView.as_view(), name="property-paragraph-override-list"),
    path("api/site-settings/", SiteSettingsView.as_view(), name="site-settings"),
    path("api/team-members/", TeamMemberListView.as_view(), name="team-member-list"),
    path("api/testimonials/", TestimonialListView.as_view(), name="testimonial-list"),
    path("api/about-tabs/", AboutTabListView.as_view(), name="about-tab-list"),
    path("api/features/", FeatureListView.as_view(), name="feature-list"),
    path("api/contact-messages/", ContactMessageCreateView.as_view(), name="contact-message-create"),
    path("api/why-choose-features/", WhyChooseFeatureListView.as_view(), name="why-choose-feature-list"),
    path("api/why-choose-section/", WhyChooseSectionView.as_view(), name="why-choose-section"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
