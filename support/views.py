from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Message
from .serializers import MessageSerializer, CreateMessageSerializer
from rest_framework import status
from django.utils.timezone import now


class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, reply=None )

class ReplyMessageView(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated] 
    def perform_update(self, serializer):
            serializer.save(replied_at=now())
        
class ListMessagesView(generics.ListAPIView):
        queryset = Message.objects.all()
        serializer_class = MessageSerializer
        permission_classes = [permissions.IsAuthenticated,]
    