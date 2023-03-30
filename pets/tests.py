from django.test import TestCase
from models import *
from django.contrib.auth import get_user_model

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
