from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=255)  # Optional name for the level
    time = models.PositiveIntegerField(help_text="Time in seconds")
    materials = models.JSONField(help_text="List of material codes")
    target = models.JSONField(help_text="Target dictionary for materials")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or f"Level {self.id}"
