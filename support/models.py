from django.db import models
# from django.contrib.auth.models import User
from Auth.models import CustomUser
# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="messages" )
    message = models.TextField(max_length=1024, null=False)
    reply = models.TextField(max_length=1024, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for the user's message
    replied_at = models.DateTimeField(null=True, blank=True)  # Timestamp for the admin's reply
    
    def __str__(self):
        return f"Message from{self.user}: {self.message}\npReply:{self.reply}"