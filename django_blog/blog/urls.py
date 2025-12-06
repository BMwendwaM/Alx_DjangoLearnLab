from django.urls import path
from . import views

# URL patterns for post function

urlpatterns = [
    path("", views.home, name="home"),
]