from rest_framework import serializers
from cafe.models import RecipeItem, Ingredient, Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'title', 'description']

class RecipeItemSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = RecipeItem
        fields = ['id', 'ingredient', 'quantity']
class RecipeSerializer(serializers.ModelSerializer):
    items = RecipeItemSerializer(source='recipeitem_set', many=True) # Assuming the reverse relation is named 'recipeitem_set'

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'unit_price', 'items']
