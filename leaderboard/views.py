from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Player
from .serializers import PlayerSerializer

# Fetch the leaderboard (GET)
@api_view(['GET'])
def leaderboard(request):
    top_players = Player.objects.order_by('-score')[:10]  # Top 10 players
    serializer = PlayerSerializer(top_players, many=True)
    return Response(serializer.data)

# Submit a new score (POST)
@api_view(['POST'])
def submit_score(request):
    serializer = PlayerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)