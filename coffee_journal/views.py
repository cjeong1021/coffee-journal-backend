from queue import PriorityQueue
from rest_framework import generics
from .serializers import ProfileSerializer, CoffeeSerializer
from .models import Profile, Coffee
from rest_framework.permissions import BasePermission, IsAuthenticated


class WritePermission(BasePermission):
    message = "Editing Coffee restricted to author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CoffeeList(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer


class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
