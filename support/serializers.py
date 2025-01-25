from rest_framework import serializers
from .models import Message
from django.utils.timezone import now

class MessageSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ['id', 'user', "username", 'message', 'reply', 'created_at', 'replied_at']
        read_only_fields = ['id', 'user', "username",'message', 'created_at', 'replied_at']
    def update(self, instance, validated_data):
        if 'reply' in validated_data:
            instance.reply = validated_data['reply']
            instance.replied_at = now()
        instance.save()
        return instance
    def get_username(self, obj):
        return obj.user.username if obj.user else None    

class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message'] 