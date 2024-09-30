from django.contrib.auth.models import User
from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)


class Cat(models.Model):
    name = models.CharField(max_length=100)
    # breed = models.ForeignKey(Breed, related_name='kittens', on_delete=models.CASCADE)
    breed = models.CharField(max_length=55)
    color = models.CharField(max_length=55)
    age = models.IntegerField()
    description = models.TextField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
