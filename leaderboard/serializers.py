from rest_framework import serializers
from .models import UserScore
from rest_framework import serializers

class UserScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserScore
        fields = ['username', 'level', 'score']
