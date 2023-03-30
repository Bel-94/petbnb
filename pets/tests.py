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

#Location model tests
class LocationModelTest(TestCase):
    '''In the test for the Location model, I used a class method setUpClass() to set up the required data for the tests to run. This is because each test method in the test class should be independent and not rely on data created in another test method.
    Using setUpClass() ensures that the data is created only once before any of the test methods are run, which makes the tests faster and more efficient. Additionally, if there are a lot of tests that require the same setup, using setUpClass() can help reduce code duplication.'''
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create_user(username='johndoe', password='12345')
        Location.objects.create(user=user, street_address='123 Main St', area='Downtown', county='City County', postal_code='12345')

    def test_street_address_label(self):
        location = Location.objects.get(id=1)
        field_label = location._meta.get_field('street_address').verbose_name
        self.assertEqual(field_label, 'street address')

    def test_area_label(self):
        location = Location.objects.get(id=1)
        field_label = location._meta.get_field('area').verbose_name
        self.assertEqual(field_label, 'area')

    def test_county_label(self):
        location = Location.objects.get(id=1)
        field_label = location._meta.get_field('county').verbose_name
        self.assertEqual(field_label, 'county')

    def test_postal_code_label(self):
        location = Location.objects.get(id=1)
        field_label = location._meta.get_field('postal_code').verbose_name
        self.assertEqual(field_label, 'postal code')

    def test_street_address_max_length(self):
        location = Location.objects.get(id=1)
        max_length = location._meta.get_field('street_address').max_length
        self.assertEqual(max_length, 255)

    def test_area_max_length(self):
        location = Location.objects.get(id=1)
        max_length = location._meta.get_field('area').max_length
        self.assertEqual(max_length, 100)

    def test_county_max_length(self):
        location = Location.objects.get(id=1)
        max_length = location._meta.get_field('county').max_length
        self.assertEqual(max_length, 100)

    def test_postal_code_max_length(self):
        location = Location.objects.get(id=1)
        max_length = location._meta.get_field('postal_code').max_length
        self.assertEqual(max_length, 20)

    def test_object_name_is_address(self):
        location = Location.objects.get(id=1)
        expected_object_name = f"{location.street_address}, {location.area}, {location.county}, {location.postal_code}"
        self.assertEqual(str(location), expected_object_name)

#RateandReview model tests
class RateandReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user = User.objects.create_user(username='user', password='password')
        provider = ServiceProvider.objects.create(name='provider')
        service = Service.objects.create(name='service', provider=provider)
        RateandReview.objects.create(user=user, service_provider=provider, service=service, rating=4, review='Great service!')

    '''tests the __str__ method of the RateandReview model to ensure that it returns the expected string representation.'''
    def test_str_method(self):
        review = RateandReview.objects.get(id=1)
        expected_str = f"{review.user} rated {review.service_provider.name}'s {review.service.name} {review.rating} stars on {review.created_at}"
        self.assertEqual(str(review), expected_str)