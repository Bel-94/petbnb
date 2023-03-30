from django.test import TestCase
from models import *
from django.contrib.auth import get_user_model
from datetime import datetime

# Create your tests here.
# User Model Tests
class UserModelTest(TestCase):
    def setUp(self):
        ''' get_user_model function from Django's built-in auth module to retrieve the custom User model'''
        self.User = get_user_model()
        self.superuser = self.User.objects.create_superuser(
            username='admin',
            password='password'
        )
        self.petowner = self.User.objects.create_user(
            username='petowner',
            password='password',
            is_petowner=True
        )
        self.serviceprovider = self.User.objects.create_user(
            username='serviceprovider',
            password='password',
            is_serviceprovider=True
        )

    '''The test_user_types method tests that each user has the correct user type attribute (is_superuser, is_petowner, or is_serviceprovider) set to True, and that each user has the other user type attributes set to False.'''
    def test_user_types(self):
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.petowner.is_petowner)
        self.assertTrue(self.serviceprovider.is_serviceprovider)
        self.assertFalse(self.superuser.is_petowner)
        self.assertFalse(self.petowner.is_serviceprovider)
        self.assertFalse(self.serviceprovider.is_petowner)
        self.assertFalse(self.serviceprovider.is_superuser)

# Booking model tests
class BookingModelTest(TestCase):
    def setUp(self):
        pet_owner = PetOwner.objects.create(user_id=1, name='John Doe')
        service_provider = ServiceProvider.objects.create(user_id=2, name='Jane Doe')
        service = Service.objects.create(name='Pet grooming', description='Service for grooming pets', price=20.0)
        pet = Pet.objects.create(name='Fluffy', species='Dog', breed='Poodle', age=5, gender='Female', owner=pet_owner)
        date = datetime.now().date()
        start_time = datetime.now().time()
        end_time = (datetime.now() + datetime.timedelta(hours=2)).time()
        booking = Booking.objects.create(pet_owner=pet_owner, service_provider=service_provider, service=service, pet=pet, date=date, start_time=start_time, end_time=end_time)

    def test_booking_str(self):
        booking = Booking.objects.get(id=1)
        self.assertEqual(str(booking), "John Doe booked Pet grooming with Jane Doe on " + datetime.now().date().strftime('%Y-%m-%d') + " at " + datetime.now().time().strftime('%H:%M:%S'))

    def test_booking_is_confirmed(self):
        booking = Booking.objects.get(id=1)
        self.assertFalse(booking.is_confirmed)

    def test_booking_created_at(self):
        booking = Booking.objects.get(id=1)
        self.assertIsNotNone(booking.created_at)
