from django.urls import path, include
from apps.views import main

urlpatterns = [
    path("home", main, name="main"),
]
