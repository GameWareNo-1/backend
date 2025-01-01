from django.urls import path
from .views import PlayerRegistrationView

urlpatterns = [
    path('register/player/', PlayerRegistrationView.as_view(), name='register_player'),
]