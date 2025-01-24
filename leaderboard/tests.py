from rest_framework.test import APITestCase
from rest_framework import status
from .models import Player

# Create your tests here.
class LeaderboardTests(APITestCase):


    def setUp(self):
        # Create some players to test with
        Player.objects.create(name='Player1', score=100)
        Player.objects.create(name='Player2', score=150)
        Player.objects.create(name='Player3', score=200)
        Player.objects.create(name='Player4', score=50)
        Player.objects.create(name='Player5', score=300)
