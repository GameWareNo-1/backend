from rest_framework import serializers
from .models import Message
from django.utils.timezone import now

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'message', 'reply', 'created_at', 'replied_at']
        read_only_fields = ['id', 'created_at', 'replied_at', "message", "user"]
    def update(self, instance, validated_data):
        if 'reply' in validated_data:
            instance.reply = validated_data['reply']
            instance.replied_at = now()
        instance.save()
        return instance
    

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message'] 