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

class Booking(models.Model):
    pet_owner = models.ForeignKey(PetOwner, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.pet_owner.user.username} booked {self.service.name} with {self.service_provider.name} on {self.date} at {self.start_time}"

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    area = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return f"{self.street_address}, {self.area}, {self.county}, {self.postal_code}"

class RateandReview(models.Model):
    pass