
from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from faker import Faker
from listing.models import Listing,Booking,Review
from django.contrib.auth.models import User
import random



class Command(BaseCommand):

    help = 'Seeds the database with fake data for the ALX Travel App'

    def handle(self, *args, **options):

        fake = Faker()

        self.stdout.write(self.style.NOTICE('Starting to seed the database...'))


        all_users = []
        all_listing = []

        self.stdout.write('Creating 10 fake users...')

        for _ in range(10):

            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            all_users.append(user)

        self.stdout.write('Creating 10 fake listings...')
        for _ in range(15):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=fake.random_int(min=50, max=500),
                location=fake.city()
            )
            all_listing.append(listing)

        # --- 6. CREATE "CHILD" DATA (BOOKINGS & REVIEWS) ---
        self.stdout.write('Creating 50 fake bookings...')
        for _ in range(50):
            # Pick a random user and listing
            random_user = random.choice(all_users)
            random_listing = random.choice(all_listing)

            # Create fake dates
            today = timezone.now().date()
            start_date = fake.date_between(start_date=today, end_date="+3M")
            end_date = start_date + datetime.timedelta(days=random.randint(2, 7))

            Booking.objects.create(
                listing=random_listing,
                user=random_user,
                start_date=start_date,
                end_date=end_date
            )

        self.stdout.write('Creating 100 fake reviews...')
        for _ in range(100):
            # Pick a random user and listing
            random_user = random.choice(all_users)
            random_listing = random.choice(all_listing)
            
            Review.objects.create(
                listing=random_listing,
                user=random_user,
                rating=random.randint(3, 5), 
                comment=fake.paragraph(nb_sentences=2)
            )

        
        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded the database with 10 users, 30 listings, 50 bookings, and 100 reviews.'
        ))
                
