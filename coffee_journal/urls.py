from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", views.UserList.as_view(), name="user_list"),
    path("users/<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    path("coffees/", views.CoffeeList.as_view(), name="coffee_list"),
    path("coffees/<int:pk>", views.CoffeeDetail.as_view(), name="coffee_detail"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
