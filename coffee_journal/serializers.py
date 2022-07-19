from rest_framework import serializers
from .models import Profile, Coffee


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "id", "name", "fav_roast", "brew_method")


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = (
            "user",
            "id",
            "name",
            "roast",
            "origin",
            "notes",
            "brew_method",
            "image",
        )
