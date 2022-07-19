from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("profiles/", views.ProfileList.as_view(), name="profile_list"),
    path("profiles/<int:pk>", views.ProfileDetail.as_view(), name="profile_detail"),
    path("coffees/", views.CoffeeList.as_view(), name="coffee_list"),
    path("coffees/<int:pk>", views.CoffeeDetail.as_view(), name="coffee_detail"),
    path(
        "preview/profiles/",
        views.ProfileListPreview.as_view(),
        name="profile_list_preview",
    ),
    path(
        "preview/coffees/",
        views.CoffeeListPreview.as_view(),
        name="coffee_list_preview",
    ),
]
