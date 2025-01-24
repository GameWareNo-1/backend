from django.urls import path
from .views import PlayerListView

urlpatterns = [
    path('players/', PlayerListView.as_view(), name='player_list'),
]