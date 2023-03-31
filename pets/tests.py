
from django.test import TestCase
from .models import Pet, GroomingService, VeterinaryService, BoardingService, ServiceProvider, Payment

class PetTestCase(TestCase):
    def setUp(self):
        Pet.objects.create(name="Buddy", category="Dog", breed="Golden Retriever", age=3, gender="Male", medical_history="None")

    def test_pet_str(self):
        pet = Pet.objects.get(name="Buddy")
        self.assertEqual(str(pet), "Buddy")

    def test_pet_attributes(self):
        pet = Pet.objects.get(name="Buddy")
        self.assertEqual(pet.category, "Dog")
        self.assertEqual(pet.breed, "Golden Retriever")
        self.assertEqual(pet.age, 3)
        self.assertEqual(pet.gender, "Male")
        self.assertEqual(pet.medical_history, "None")


class GroomingServiceTestCase(TestCase):
    def setUp(self):
        GroomingService.objects.create(name="Basic Grooming", price=50.00, duration="1 hour", description="Includes a bath, brush, and trim")

    def test_grooming_service_str(self):
        service = GroomingService.objects.get(name="Basic Grooming")
        self.assertEqual(str(service), "Basic Grooming")

    def test_grooming_service_attributes(self):
        service = GroomingService.objects.get(name="Basic Grooming")
        self.assertEqual(service.price, 50.00)
        self.assertEqual(service.duration, "1 hour")
        self.assertEqual(service.description, "Includes a bath, brush, and trim")



class VeterinaryServiceTestCase(TestCase):
    def setUp(self):
        VeterinaryService.objects.create(name="Annual Checkup", price=100.00, duration="30 minutes", description="Includes a full physical exam and vaccinations")

    def test_veterinary_service_str(self):
        service = VeterinaryService.objects.get(name="Annual Checkup")
        self.assertEqual(str(service), "Annual Checkup")

    def test_veterinary_service_attributes(self):
        service = VeterinaryService.objects.get(name="Annual Checkup")
        self.assertEqual(service.price, 100.00)
        self.assertEqual(service.duration, "30 minutes")
        self.assertEqual(service.description, "Includes a full physical exam and vaccinations")

class BoardingServiceTestCase(TestCase):
    def setUp(self):
        BoardingService.objects.create(name="Standard Boarding", price=25.00, duration="Per night", description="Includes a private room and daily walks")

    def test_boarding_service_str(self):
        service = BoardingService.objects.get(name="Standard Boarding")
        self.assertEqual(str(service), "Standard Boarding")

    def test_boarding_service_attributes(self):
        service = BoardingService.objects.get(name="Standard Boarding")
        self.assertEqual(service.price, 25.00)
        self.assertEqual(service.duration, "Per night")
        self.assertEqual(service.description, "Includes a private room and daily walks")



class ServiceProviderTestCase(TestCase):
    def setUp(self):
        self.grooming_service = GroomingService.objects.create(name="Test Grooming Service", price=25.00, duration="1 hour", description="Test description")
        self.veterinary_service = VeterinaryService.objects.create(name="Test Veterinary Service", price=50.00, duration="30 minutes", description="Test description")
        self.boarding_service = BoardingService.objects.create(name="Test Boarding Service", price=100.00, duration="1 day", description="Test description")
        self.service_provider = ServiceProvider.objects.create(name="Test Service Provider", GroomingService=self.grooming_service, VeterinaryService=self.veterinary_service, BoardingService=self.boarding_service, capacity=10, availability=True, contact_info="test@example.com")

    def test_service_provider_creation(self):
        self.assertTrue(isinstance(self.service_provider, ServiceProvider))
        self.assertEqual(self.service_provider.__str__(), self.service_provider.location)

    def test_service_provider_attributes(self):
        self.assertEqual(self.service_provider.name, "Test Service Provider")
        self.assertEqual(self.service_provider.GroomingService, self.grooming_service)
        self.assertEqual(self.service_provider.VeterinaryService, self.veterinary_service)
        self.assertEqual(self.service_provider.BoardingService, self.boarding_service)
        self.assertEqual(self.service_provider.capacity, 10)
        self.assertEqual(self.service_provider.availability, True)
        self.assertEqual(self.service_provider.contact_info, "test@example.com")



class PaymentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.payment = Payment.objects.create(user=self.user, transaction_amount=50.00, transaction_date="2023-03-27")

    def test_payment_creation(self):
        self.assertTrue(isinstance(self.payment, Payment))
        self.assertEqual(self.payment.__str__(), f"{self.user} - {self.payment.transaction_amount}")

    def test_payment_attributes(self):
        self.assertEqual(self.payment.user, self.user)
        self.assertEqual(self.payment.transaction_amount, 50.00)
        self.assertEqual(str(self.payment.transaction_date), "2023-03-27")
