from rest_framework.generics import ListAPIView
from Auth.models import CustomUser
from .serializers import PlayerSerializer

class PlayerListView(ListAPIView):
    queryset = CustomUser.objects.filter(user_type='player').order_by("-aggregate_score")
    serializer_class = PlayerSerializer
