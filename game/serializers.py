from rest_framework import serializers
from Auth.models import CustomUser

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', "aggregate_score"]