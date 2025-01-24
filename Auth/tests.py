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

    def test_player_registration_success(self):
        # Test successful player registration
        data = {
            'username': 'player1',
            'password': 'password123',
            'email': 'player1@example.com',
        }