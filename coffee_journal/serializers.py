from rest_framework import serializers
from .models import Profile, Coffee


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    coffees = serializers.HyperlinkedRelatedField(
        view_name="coffee_detail", many=True, read_only=True
    )

    class Meta:
        model = Profile
        fields = ("id", "name", "fav_roast", "brew_method", "coffees")


class CoffeeSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name="user_detail", many=False, read_only=True
    )

    class Meta:
        model = Coffee
        fields = ("id", "name", "roast", "origin", "notes", "brew_method", "user")
