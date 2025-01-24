from rest_framework import serializers
from .models import Level
from rest_framework.exceptions import ValidationError

class LevelSerializer(serializers.ModelSerializer):
    def validate_materials(self, value):
        if not isinstance(value, list):
            raise ValidationError("Materials must be a list.")
        return value
    
    def validate_target(self, value):
        if sum(value.values()) != 4:
            raise ValidationError("Sum of target values must equal 4.")
        return value

    class Meta:
        model = Level
        fields = '__all__'
