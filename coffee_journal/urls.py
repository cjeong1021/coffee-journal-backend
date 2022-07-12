from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    path("coffees/", views.CoffeeList.as_view(), name="coffee_list"),
    path("coffees/<int:pk>", views.CoffeeDetail.as_view(), name="coffee_detail"),
]
