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


        # Create a sample message for testing reply functionality
        self.message = Message.objects.create(user=self.user, message="This is a test message", reply=None)

        # URL definitions
        self.create_url = reverse('create-message')
        self.list_url = reverse('list-message')
        self.reply_url = reverse('reply-message', kwargs={'pk': self.message.pk})


    def test_create_message_authenticated(self):
        # Test that authenticated user can create a message
        self.client.login(username='user1', password='password123')
        data = {'message': 'This is a new message'}
        response = self.client.post(self.create_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 2)  # There should now be 2 messages
        self.assertEqual(response.data['message'], 'This is a new message')
        self.assertEqual(response.data['user'], self.user.id)


    def test_create_message_unauthenticated(self):
        # Test that unauthenticated user cannot create a message
        data = {'message': 'This is a new message'}
        response = self.client.post(self.create_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Message.objects.count(), 1)



    def test_list_messages_authenticated(self):
        # Test that authenticated user can list all messages
        self.client.login(username='user1', password='password123')
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one message should exist
        self.assertEqual(response.data[0]['message'], self.message.message)



    def test_list_messages_unauthenticated(self):
        # Test that unauthenticated user cannot list messages
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_reply_message_authenticated(self):
        # Test that authenticated user can reply to a message
        self.client.login(username='admin', password='password123')
        data = {'reply': 'This is a reply to the message'}
        response = self.client.put(self.reply_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reply'], 'This is a reply to the message')
        self.assertIsNotNone(response.data['replied_at'])  # Ensure replied_at is set

        # Verify the message in the database has been updated with the reply
        message = Message.objects.get(pk=self.message.pk)
        self.assertEqual(message.reply, 'This is a reply to the message')