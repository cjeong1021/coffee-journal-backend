from rest_framework import generics
from .serializers import UserSerializer, CoffeeSerializer
from .models import User, Coffee
from rest_framework.permissions import BasePermission, IsAuthenticated


class WritePermission(BasePermission):
    message = "Editing Coffee restricted to author only"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoffeeList(generics.ListCreateAPIView):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer


class CoffeeDetail(generics.RetrieveUpdateDestroyAPIView, WritePermission):
    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer
