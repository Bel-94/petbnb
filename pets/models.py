from django.db import models
from django.contrib.auth.models import User

# #Incase we use a customized user.
# from django.contrib.auth import get_user_model
# User = get_user_model() 



class Pet(models.Model):
    #Details of the pet
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()
    # Other fields related to pet information

class Reservation(models.Model):
    #Users are able to reserve dates for their pets to get shelter or services
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    service_type = models.CharField(max_length=255)
    # Other fields related to reservation information

class Service(models.Model):
    SERVICE_TYPES = (
        ('grooming', 'Grooming'),
        ('boarding', 'Boarding'),
        ('veterinary', 'Veterinary'),
        # we can add other service types as needed
    )
    service_type = models.CharField(max_length=255, choices=SERVICE_TYPES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)
    description = models.TextField()
    # service_provider = models.ForeignKey(service_provider, on_delete=models.CASCADE)
    # Other fields related to service information

class Payment(models.Model):
    #Mode of payment for the users, more fields to be added as we progress
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    # Other fields related to payment information

class Review(models.Model):
    #Users canrate review and leave a comment for the services received
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    # Other fields related to review information

