from django.db import models
from django.contrib.auth.models import User

    
class Pet(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    medical_history = models.TextField()

    class Meta:
        verbose_name_plural = "Pets"

    def __str__(self):
        return self.name

class Shelter(models.Model):
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    contact_info = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Shelters"

    def __str__(self):
        return self.location

class GroomingService(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Grooming Services"

    def __str__(self):
        return self.name

class VeterinaryService(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Veterinary Services"

    def __str__(self):
        return self.name

class BoardingService(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Boarding Services"

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    service = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Reservations"

    def __str__(self):
        return f"{self.user} - {self.pet} - {self.service}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    class Meta:
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.user} - {self.transaction_amount}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()

    class Meta:
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"{self.user} - {self.rating}"
