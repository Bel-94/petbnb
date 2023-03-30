from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.

class User(AbstractUser):
    is_superuser = models.BooleanField(default=False),
    is_petowner = models.BooleanField(default=False),
    is_serviceprovider = models.BooleanField(default=False),

class PetOwner(models.Model):
    pass

class Pet(models.Model):
    pass

class ServiceProvider(models.Model):
    pass

class Service(models.Model):
    pass

class Appointment(models.Model):
    pass

class Booking(models.Model):
    pass

class Location(models.Model):
    pass

class RateandReview(models.Model):
    pass