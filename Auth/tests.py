from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import Group
from .models import CustomUser

# Create your tests here.
class UserRegistrationTests(APITestCase):

    # Ensure the necessary groups exist before running tests
    def setUp(self):

        Group.objects.get_or_create(name='Player')
        Group.objects.get_or_create(name='Manager')


    # Test successful player registration
    def test_player_registration_success(self):
        
        data = {
            'username': 'player1',
            'password': 'password123',
            'email': 'player1@example.com',
        }

        response = self.client.post('/custom-auth/register/player/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], f"Player user {data['username']} created successfully.")
        self.assertTrue(CustomUser.objects.filter(username=data['username']).exists())
        player = CustomUser.objects.get(username=data['username'])
        self.assertEqual(player.user_type, 'player')
        self.assertTrue(player.groups.filter(name='Player').exists())


    # Test player registration with missing fields
    def test_player_registration_missing_fields(self):
        
        data = {'username': 'player2'}
        response = self.client.post('/player/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)



    # Test successful manager registration
    def test_manager_registration_success(self):
        
        data = {
            'username': 'manager1',
            'password': 'password123',
            'email': 'manager1@example.com',
        }
        response = self.client.post('/custom-auth/register/manager/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], f"Manager user {data['username']} created successfully.")
        self.assertTrue(CustomUser.objects.filter(username=data['username']).exists())
        manager = CustomUser.objects.get(username=data['username'])
        self.assertEqual(manager.user_type, 'manager')
        self.assertTrue(manager.groups.filter(name='Manager').exists())


    # Test manager registration with missing fields
    def test_manager_registration_missing_fields(self):
        
        data = {'username': 'manager2'}
        response = self.client.post('/manager/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)