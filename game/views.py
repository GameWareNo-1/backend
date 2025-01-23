from rest_framework.generics import ListAPIView
from Auth.models import CustomUser
from .serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


def is_manager(user):
    return user.groups.filter(name='manager').exists()

class PlayerListView(ListAPIView):
    queryset = CustomUser.objects.filter(user_type='player').order_by("-aggregate_score")
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated] 
    def get(self, request, *args, **kwargs):
        # Check if the requesting user is a manager.
        if not is_manager(self.request.user):
            return Response(
                {'error': 'Not authorized. Only managers can access this resource.'},
                status=status.HTTP_403_FORBIDDEN
            )
        # If the user is a manager, proceed to return the player list.
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)        