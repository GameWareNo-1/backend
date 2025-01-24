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


    def test_leaderboard_get(self):
        # Test GET method to fetch the top 10 players
        response = self.client.get('/leaderboard/')  # Update with actual endpoint if different
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)  # We only have 5 players in the DB
        self.assertEqual(response.data[0]['name'], 'Player5')  # Top player should have highest score
        self.assertEqual(response.data[1]['name'], 'Player3')  # Next in line


    def test_submit_score_post_success(self):
        # Test POST method to submit a new player's score
        data = {'name': 'Player6', 'score': 250}
        response = self.client.post('/submit_score/', data)  # Update with actual endpoint if different
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Player6')
        self.assertEqual(response.data['score'], 250)


        # Verify that the new player has been added to the database
        player = Player.objects.get(name='Player6')
        self.assertEqual(player.score, 250)

    def test_submit_score_post_failure(self):
        # Test POST method with invalid data (missing 'name' field)
        data = {'score': 250}
        response = self.client.post('/submit_score/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)