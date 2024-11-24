from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import RecipeSerializer
from .models import Recipe


@api_view()
def Recipe_list(request):
    queryset = Recipe.objects.all()
    serialzier = RecipeSerializer(queryset, many=True)
    return Response(serialzier.data)

@api_view()
def Recipe_detail(request,id):
    recipe = get_object_or_404(Recipe, pk=id)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)
