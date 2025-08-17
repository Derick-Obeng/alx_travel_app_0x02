from django.core.management.base import BaseCommand

from alx_travel_app_0x00.alx_travel_app.listings.models import Listing


class Command(BaseCommand):
    help = 'Seed the database with sample travel listings'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Listing.objects.all().delete()

        # Sample data
        data = [
            {
                "title": "Accra City Tour",
                "description": "Experience the vibrant city life of Accra.",
                "location": "Accra, Ghana",
                "price": 150.00,
            },
            {
                "title": "Cape Coast Castle Visit",
                "description": "Explore the historic Cape Coast Castle.",
                "location": "Cape Coast, Ghana",
                "price": 100.00,
            },
            {
                "title": "Safari in Mole National Park",
                "description": "Enjoy a safari adventure with wildlife sightings.",
                "location": "Mole, Ghana",
                "price": 300.00,
            },
        ]

        for item in data:
            Listing.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully with sample listings.'))
