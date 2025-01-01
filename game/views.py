from rest_framework.generics import ListAPIView
from Auth.models import CustomUser
from .serializers import PlayerSerializer

class PlayerListView(ListAPIView):
    queryset = CustomUser.objects.filter(user_type='player')
    serializer_class = PlayerSerializer
