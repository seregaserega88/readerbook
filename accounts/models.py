from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Дополнительные поля профиля (например, язык)

    def __str__(self):
        return self.user.username
