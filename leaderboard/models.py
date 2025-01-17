from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)  # Add this field

    def __str__(self):
        return self.name
    