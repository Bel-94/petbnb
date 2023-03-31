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

class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)
    GroomingService = models.ForeignKey(GroomingService, on_delete=models.CASCADE)
    VeterinaryService = models.ForeignKey(VeterinaryService, on_delete=models.CASCADE)
    BoardingService = models.ForeignKey(BoardingService, on_delete=models.CASCADE)
    # location = models.CharField(max_length=255)  (Should be a foreignKey)
    capacity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)
    contact_info = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "ServiceProviders"

    def __str__(self):
        return self.location

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()

    class Meta:
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"{self.user} - {self.transaction_amount}"
