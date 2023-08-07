from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_characters, name = "home")
]