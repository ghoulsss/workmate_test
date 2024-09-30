from django.contrib.auth.models import User
from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=55)
    color = models.CharField(max_length=55)
    age = models.IntegerField()
    description = models.TextField(max_length=255)
    owner = models.CharField(max_length=55)

    def __str__(self):
        return self.name
