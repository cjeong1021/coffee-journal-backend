from rest_framework import serializers
from .models import Profile, Coffee


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "name", "fav_roast", "brew_method")


class CoffeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coffee
        fields = ("id", "name", "roast", "origin", "notes", "brew_method")
