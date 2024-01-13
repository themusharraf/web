from django.urls import path, include
from apps.views import main

urlpatterns = [
    path("", main, name="main"),
]
