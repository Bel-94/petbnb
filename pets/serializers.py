from rest_framework import serializers
from .models import *

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class GroomingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroomingService
        fields = '__all__'

class VeterinaryServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeterinaryService
        fields = '__all__'

class BoardingServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardingService
        fields = '__all__'

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class RateandReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateandReview
        fields = '__all__'