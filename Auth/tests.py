from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import Group
from .models import CustomUser

# Create your tests here.
class UserRegistrationTests(APITestCase):
    def setUp(self):
        # Ensure the necessary groups exist before running tests
        Group.objects.get_or_create(name='Player')
        Group.objects.get_or_create(name='Manager')