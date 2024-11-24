from rest_framework import serializers
from cafe.models import Recipe
from decimal import Decimal
class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)   

        
