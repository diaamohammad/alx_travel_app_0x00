from django.core.management.base import BaseCommand
from listings.models import Listing
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        titles = ["Cozy Apartment", "Beach House", "Mountain Cabin", "City Studio", "Luxury Villa"]

        for title in titles:
            Listing.objects.create(
                title=title,
                description=f"A beautiful {title.lower()} available for rent.",
                price=random.randint(50, 500),
                location=random.choice(["Cairo", "Alexandria", "Giza", "Hurghada"]),
            )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded with sample listings!"))
