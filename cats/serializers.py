from rest_framework import serializers
from .models import Breed, Cat


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'
