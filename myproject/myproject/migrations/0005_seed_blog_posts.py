from django.db import migrations


POSTS = [
    {
        "title": "5 Smart Steps Before Buying Your First Home",
        "slug": "five-smart-steps-before-buying-your-first-home",
        "excerpt": "A practical checklist to help first-time buyers avoid common mistakes and buy with confidence.",
        "content": (
            "Buying your first home is exciting, but it can also feel overwhelming. Start by defining a realistic "
            "budget that includes loan payments, registration costs, and moving expenses. Next, choose neighborhoods "
            "based on commute time, nearby essentials, and future development plans. Always verify legal documents "
            "such as ownership history, approval status, and tax records before you make an offer. A professional "
            "inspection can help you identify hidden structural or maintenance problems early. Finally, compare two "
            "or three properties side by side so you can make a calm and informed final decision."
        ),
        "author": "Prime Estates Editorial",
        "cover_image": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=1200&q=80",
    },
    {
        "title": "How to Stage Your Property for a Faster Sale",
        "slug": "how-to-stage-your-property-for-a-faster-sale",
        "excerpt": "Simple staging upgrades can increase buyer interest and improve your selling price.",
        "content": (
            "Home staging is one of the easiest ways to make your property stand out online and during site visits. "
            "Begin by decluttering each room so buyers can clearly see usable space. Use neutral colors, clean linens, "
            "and soft lighting to create a warm and welcoming mood. Minor fixes like repainting scuffed walls or "
            "repairing loose handles can significantly improve first impressions. Highlight focal areas such as the "
            "living room and kitchen because buyers spend the most attention there. A thoughtfully staged home often "
            "sells faster and attracts stronger offers."
        ),
        "author": "Prime Estates Editorial",
        "cover_image": "https://images.unsplash.com/photo-1494526585095-c41746248156?w=1200&q=80",
    },
    {
        "title": "Rental Market Trends to Watch This Year",
        "slug": "rental-market-trends-to-watch-this-year",
        "excerpt": "From shifting tenant preferences to pricing trends, here is what landlords should monitor.",
        "content": (
            "The rental market is changing quickly as tenant expectations evolve. Demand remains strong for homes "
            "near transit routes, schools, and mixed-use neighborhoods. Tenants increasingly look for flexible layouts, "
            "reliable internet access, and energy-efficient features that reduce utility costs. Owners who maintain "
            "their properties proactively and respond quickly to maintenance requests often retain tenants longer. "
            "Rent adjustments should be based on comparable listings, occupancy levels, and local regulations. "
            "Staying data-informed helps landlords maintain stable income while keeping vacancy risk low."
        ),
        "author": "Prime Estates Editorial",
        "cover_image": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1200&q=80",
    },
    {
        "title": "What Adds the Most Value Before Listing a Home",
        "slug": "what-adds-the-most-value-before-listing-a-home",
        "excerpt": "Focus on improvements that buyers notice first and that deliver clear return on investment.",
        "content": (
            "Not every renovation delivers equal value when preparing to sell. Start with cosmetic upgrades that are "
            "visible and affordable, such as fresh paint, modern fixtures, and improved curb appeal. Kitchens and "
            "bathrooms usually have the strongest influence on buyer decisions, so small updates there can go far. "
            "Deep cleaning, proper lighting, and organized storage can make rooms feel larger and newer. Avoid highly "
            "personalized changes that might limit buyer appeal. A balanced prep strategy helps you attract more "
            "viewings and negotiate from a stronger position."
        ),
        "author": "Prime Estates Editorial",
        "cover_image": "https://images.unsplash.com/photo-1572120360610-d971b9d7767c?w=1200&q=80",
    },
    {
        "title": "Neighborhood Checklist for Families Moving Soon",
        "slug": "neighborhood-checklist-for-families-moving-soon",
        "excerpt": "Use this family-focused checklist to compare neighborhoods before making a move.",
        "content": (
            "Choosing the right neighborhood is just as important as choosing the right house, especially for families. "
            "Begin with school quality, travel time, and access to healthcare facilities. Visit at different times of "
            "day to understand traffic flow, noise levels, and overall safety. Check availability of parks, grocery "
            "stores, and child-friendly community services nearby. Talk with local residents to learn about day-to-day "
            "living conditions that listings may not reveal. A careful neighborhood review can save time, stress, and "
            "future relocation costs."
        ),
        "author": "Prime Estates Editorial",
        "cover_image": "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
    },
]


def seed_posts(apps, schema_editor):
    Post = apps.get_model("myproject", "Post")

    for post in POSTS:
        Post.objects.update_or_create(
            slug=post["slug"],
            defaults={
                "title": post["title"],
                "excerpt": post["excerpt"],
                "content": post["content"],
                "author": post["author"],
                "cover_image": post["cover_image"],
                "is_published": True,
            },
        )


def unseed_posts(apps, schema_editor):
    Post = apps.get_model("myproject", "Post")
    Post.objects.filter(slug__in=[post["slug"] for post in POSTS]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("myproject", "0004_delete_sitecontrol"),
    ]

    operations = [
        migrations.RunPython(seed_posts, unseed_posts),
    ]
