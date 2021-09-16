from django.db import models


# модель комнаты
class Room(models.Model):
    room_name = models.CharField(max_length=100, unique=True)


# модель сообщений
class Message(models.Model):
    username = models.CharField(max_length=40)
    text = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        ordering = ('date',)
