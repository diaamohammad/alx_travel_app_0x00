from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Listing,Booking,Review
from django.utils import timezone


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email']



class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['id', 'title', 'price_per_night', 'location']



class BookingListSerializer(serializers.ModelSerializer):

    listing = ListingSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'start_date', 'end_date', 'booked_at']


class BookingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['listing', 'start_date', 'end_date']

    def validate(self, data):

        if data['start_date'] > data['end_date']:
            
            raise serializers.ValidationError("End date must be after start date.")
        
        if data['start_date'] < timezone.now().date():

            raise serializers.ValidationError("Start date cannot be in the past.")
        
        existing_bookings = Booking.objects.filter(
            listing=data['listing'],
            start_date__lt=data['end_date'],
            end_date__gt=data['start_date']
        ).exists()
        
        if existing_bookings:
            raise serializers.ValidationError("This listing is already booked for the selected dates.")
            
        return data

class ReviewSerializer(serializers.ModelSerializer):
     
     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
     listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
     username = serializers.ReadOnlyField(source='user.username')

     class Meta:
        model = Review
        fields = ['id', 'listing', 'user', 'username', 'rating', 'comment', 'created_at']