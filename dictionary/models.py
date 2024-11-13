from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    is_learned = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='words')

    def __str__(self):
        return self.word
from django.db import models

# Create your models here.
