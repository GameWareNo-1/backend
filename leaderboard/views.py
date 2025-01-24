from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserScore
from django.db.models import Sum
from .serializers import UserScoreSerializer
class SubmitScoreAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        level = request.data.get('level')
        score = request.data.get('score')

        if not username or not level or not score:
            return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_score = UserScore.objects.get(username=username, level=level)
            if score > user_score.score:
                user_score.score = score
                user_score.save()
        except UserScore.DoesNotExist:
            UserScore.objects.create(username=username, level=level, score=score)

        return Response({'message': 'Score submitted successfully'}, status=status.HTTP_200_OK)

class LeaderboardAPIView(APIView):
    def get(self, request):
        top_scorers = UserScore.objects.values('username').annotate(
            total_score=Sum('score')
        ).order_by('-total_score')

        return Response(top_scorers, status=status.HTTP_200_OK)
