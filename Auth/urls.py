from django.urls import path
from .views import PlayerRegistrationView,ManagerRegistrationView

urlpatterns = [
    path('register/player/', PlayerRegistrationView.as_view(), name='register_player'),
    path('register/manager/', ManagerRegistrationView.as_view(), name='register_manager'),
]