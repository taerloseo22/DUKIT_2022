from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=30,null=False, blank=False)
    git = models.CharField(max_length=30)

    def __str__(self):
        return self.username

