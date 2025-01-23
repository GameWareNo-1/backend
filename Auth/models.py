from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('manager', 'Manager'),
        ('player', 'Player'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    aggregate_score  = models.DecimalField(max_digits=5, decimal_places=2, default=0)