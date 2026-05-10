"""
Migration 0016 – seed the 5 hardcoded local properties into the DB.

After this migration every property is editable (including price) from
Django admin at /admin/myproject/property/.
The frontend will then show ONLY backend data when the API is reachable,
so any admin change is immediately reflected on the site.
"""
from django.db import migrations

LOCAL_PROPERTIES = [
    {
        "title": "Modern Villa, California",
        "city": "Los Angeles",
        "type": "villa",
        "status": "sale",
        "price": 1250000,
        "beds": 4,
        "baths": 3,
        "sqft": 3200,
        "featured": True,
        "images": [
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=1200&q=80",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=1200&q=80",
            "https://images.unsplash.com/photo-1600566753151-384129cf4e3e?w=1200&q=80",
        ],
        "amenities": ["Garden", "Garage", "Pool", "Security"],
        "description": "Open-plan living with floor-to-ceiling glass, chef's kitchen, and landscaped yard.",
    },
    {
        "title": "Luxury Penthouse, New York",
        "city": "New York",
        "type": "apartment",
        "status": "sale",
        "price": 2100000,
        "beds": 3,
        "baths": 2,
        "sqft": 2400,
        "featured": True,
        "images": [
            "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=1200&q=80",
            "https://images.unsplash.com/photo-1494526585095-c41746248156?w=1200&q=80",
            "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=1200&q=80",
        ],
        "amenities": ["Concierge", "Gym", "Terrace", "Parking"],
        "description": "Skyline views, private terrace, concierge access, and premium finishes throughout.",
    },
    {
        "title": "Family Home, Austin",
        "city": "Austin",
        "type": "townhome",
        "status": "sale",
        "price": 845000,
        "beds": 4,
        "baths": 3,
        "sqft": 2800,
        "featured": True,
        "images": [
            "https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=1200&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1200&q=80",
            "https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=1200&q=80",
        ],
        "amenities": ["Backyard", "Storage", "School Nearby", "EV Charging"],
        "description": "Spacious layouts, updated systems, and a backyard made for family gatherings.",
    },
    {
        "title": "Waterfront Condo, Miami",
        "city": "Miami",
        "type": "condo",
        "status": "rent",
        "price": 3800,
        "beds": 2,
        "baths": 2,
        "sqft": 1300,
        "featured": False,
        "images": [
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&q=80",
            "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=1200&q=80",
            "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1200&q=80",
        ],
        "amenities": ["Sea View", "Pool", "Doorman", "Gym"],
        "description": "Comfortable coastal living with full amenities and easy beach access.",
    },
    {
        "title": "Urban Loft, Chicago",
        "city": "Chicago",
        "type": "apartment",
        "status": "rent",
        "price": 2900,
        "beds": 2,
        "baths": 2,
        "sqft": 1900,
        "featured": False,
        "images": [
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=80",
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=1200&q=80",
            "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1200&q=80",
        ],
        "amenities": ["Elevator", "Balcony", "Pet Friendly", "Parking"],
        "description": "Stylish loft with exposed brick, high ceilings, and modern appliances.",
    },
]


def seed_properties(apps, schema_editor):
    Property = apps.get_model("myproject", "Property")
    # Only seed if the table is completely empty to avoid duplicates
    if not Property.objects.exists():
        for data in LOCAL_PROPERTIES:
            Property.objects.create(**data)


def unseed_properties(apps, schema_editor):
    Property = apps.get_model("myproject", "Property")
    titles = [p["title"] for p in LOCAL_PROPERTIES]
    Property.objects.filter(title__in=titles).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("myproject", "0015_sitesettings_properties_page"),
    ]

    operations = [
        migrations.RunPython(seed_properties, reverse_code=unseed_properties),
    ]
