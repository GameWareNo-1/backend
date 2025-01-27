
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from leaderboard.models import UserScore

class UserScoreTests(TestCase):

    def test_submit_score_create_new_score(self):
        url = reverse('submit_score')  # Use named URL
        data = {'username': 'player1', 'level': 1, 'score': 100}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserScore.objects.count(), 1)

    def test_submit_score_update_existing_score(self):
        UserScore.objects.create(username='player1', level=1, score=50)
        url = reverse('submit_score')
        data = {'username': 'player1', 'level': 1, 'score': 100}
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UserScore.objects.get(username='player1', level=1).score, 100)

    def test_submit_score_invalid_data(self):
        url = reverse('submit_score')
        data = {'username': 'player1'}  # Missing required fields
        response = self.client.post(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_leaderboard(self):
        UserScore.objects.create(username='player1', level=1, score=100)
        UserScore.objects.create(username='player2', level=2, score=150)
        url = reverse('top_score')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_leaderboard_empty(self):
        url = reverse('top_score')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
