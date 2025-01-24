from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Level
from .serializers import LevelSerializer


class LevelViewSet(viewsets.ViewSet):
    def list(self, request):
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            level = Level.objects.get(pk=pk)
            serializer = LevelSerializer(level)
            return Response(serializer.data)
        except Level.DoesNotExist:
            return Response({"error": "Level not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            level = Level.objects.get(pk=pk)
            level.delete()
            return Response({"message": "Level deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Level.DoesNotExist:
            return Response({"error": "Level not found"}, status=status.HTTP_404_NOT_FOUND)
