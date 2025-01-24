from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Message
from rest_framework.reverse import reverse

# Create your tests here.
class SupportAppTests(APITestCase):

    # create test users
    def setUp(self):

        self.user = get_user_model().objects.create_user(username='user1', password='password123')
        self.admin = get_user_model().objects.create_superuser(username='admin', password='password123')


