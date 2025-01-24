from rest_framework.test import APITestCase
from rest_framework import status
from .models import Player

# Create your tests here.
class LeaderboardTests(APITestCase):



    # create some players to test with
    def setUp(self):
        
        Player.objects.create(name='Player1', score=100)
        Player.objects.create(name='Player2', score=150)
        Player.objects.create(name='Player3', score=200)
        Player.objects.create(name='Player4', score=50)
        Player.objects.create(name='Player5', score=300)

    # Test GET method to fetch the top 10 players
    def test_leaderboard_get(self):
        
        response = self.client.get('/leaderboard/')  # Update with actual endpoint if different
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)  # We only have 5 players in the DB
        self.assertEqual(response.data[0]['name'], 'Player5')  # Top player should have highest score
        self.assertEqual(response.data[1]['name'], 'Player3')  # Next in line


    # Test POST method to submit a new player's score
    def test_submit_score_post_success(self):
        
        data = {'name': 'Player6', 'score': 250}
        response = self.client.post('/submit_score/', data)  # Update with actual endpoint if different
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Player6')
        self.assertEqual(response.data['score'], 250)


        # Verify that the new player has been added to the database
        player = Player.objects.get(name='Player6')
        self.assertEqual(player.score, 250)

    # Test POST method with invalid data (missing 'name' field)
    def test_submit_score_post_failure(self):
        
        data = {'score': 250}
        response = self.client.post('/submit_score/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)

    # Test GET method when no players exist
    def test_leaderboard_with_no_players(self):
        
        Player.objects.all().delete()  # Delete all players
        response = self.client.get('/leaderboard/')  # Update with actual endpoint if different
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)