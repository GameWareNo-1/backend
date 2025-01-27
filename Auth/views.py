from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser


class PlayerRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        player_user = CustomUser.objects.create_user(username=username, email=email, password=password, user_type='player')

        # Assign the user to the Player group
        player_group, _ = Group.objects.get_or_create(name='Player')
        player_user.groups.add(player_group)

        refresh = RefreshToken.for_user(player_user)
        access = refresh.access_token
        return Response({'message': f'Manager user {username} created successfully.',
                         'access': str(access),
                         'refresh': str(refresh)},
                        status=status.HTTP_201_CREATED)

class ManagerRegistrationView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        manager_user = CustomUser.objects.create_user(username=username, email=email, password=password, user_type='manager')

        # Assign the user to the manager group
        manager_group, _ = Group.objects.get_or_create(name='manager')
        manager_user.groups.add(manager_group)

        refresh = RefreshToken.for_user(manager_user)
        access = refresh.access_token
        return Response({'message': f'Manager user {username} created successfully.'}, status=status.HTTP_201_CREATED)

    
        """
        
        {
            "username": "player",
            "password": "password",
            "email": "aa@aa.cc"
        }
        
        """
        
            