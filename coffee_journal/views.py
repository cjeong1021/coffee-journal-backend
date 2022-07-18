from queue import PriorityQueue
from rest_framework import generics
from .serializers import ProfileSerializer, CoffeeSerializer
from .models import Profile, Coffee
from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)


class WritePermission(BasePermission):
    message = "Editing and posting restricted to author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    permission_classes = [WritePermission]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CoffeeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Coffee.objects.filter(user=user)


class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    permission_classes = [WritePermission]
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
