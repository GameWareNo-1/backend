from django.db import models

class UserScore(models.Model):
    username = models.CharField(max_length=100)
    level = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        unique_together = ('username', 'level')
