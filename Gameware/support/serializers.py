from rest_framework import serializers
from .models import Message
from datetime import timezone
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'user', 'message', 'reply', 'created_at', 'replied_at']
        read_only_fields = ['id', 'created_at', 'replied_at']

    def update(self, instance, validated_data):
        # Only allow `reply` and `replied_at` fields to be updated
        if 'reply' in validated_data:
            instance.reply = validated_data['reply']
            instance.replied_at = timezone.now()
        instance.save()
        return instance