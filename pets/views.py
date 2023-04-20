from django.shortcuts import render, redirect
from django.http.response import HttpResponse, Http404
from .models import *


# Create your views here.
def Index(request):
    pets = Pet.objects.all()
    grooming_services = GroomingService.objects.all()
    veterinary_services = VeterinaryService.objects.all()
    boarding_services = BoardingService.objects.all()
    service_providers = ServiceProvider.objects.all()
    bookings = Booking.objects.all()
    payments = Payment.objects.all()
    locations = Location.objects.all()
    reviews = RateandReview.objects.all()

    context = {
        'pets': pets,
        'grooming_services': grooming_services,
        'veterinary_services': veterinary_services,
        'boarding_services': boarding_services,
        'service_providers': service_providers,
        'bookings': bookings,
        'payments': payments,
        'locations': locations,
        'reviews': reviews,
    }
    return render(request, 'main/index.html', context)
