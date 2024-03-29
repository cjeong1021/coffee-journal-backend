from queue import PriorityQueue
from urllib import request
from rest_framework import generics
from .serializers import ProfileSerializer, CoffeeSerializer
from .models import Profile, Coffee
from django.http import HttpRequest, JsonResponse, HttpResponse
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


class ProfileList(generics.ListCreateAPIView, WritePermission):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Profile.objects.filter(user=user)

    def create(self, request, **kwargs):
        serializer = ProfileSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return JsonResponse(request.data)
        return JsonResponse(request.data)


class CoffeeList(generics.ListCreateAPIView, WritePermission):
    permission_classes = [IsAuthenticated]
    serializer_class = CoffeeSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Coffee.objects.filter(user=user)

    def create(self, request, **kwargs):
        serializer = CoffeeSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return JsonResponse(request.data)


class CoffeeListPreview(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CoffeeSerializer
    queryset = Coffee.objects.all()


class ProfileListPreview(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    permission_classes = [WritePermission]
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Profile.objects.filter(user=user)


class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    permission_classes = [WritePermission]
    serializer_class = CoffeeSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Coffee.objects.filter(user=user)
