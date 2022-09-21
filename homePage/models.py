from datetime import datetime
from django.db import models


# Create your models here.


class UserDetails(models.Model):
    user_Id = models.CharField(max_length=5)
    user_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user_name)


class GameNumber(models.Model):
    ticket_number = models.CharField(blank=True, max_length=255)
    game_week = models.CharField(blank=True, max_length=255)
    user_game = models.CharField(blank=True, max_length=255)
    current_user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.current_user)
