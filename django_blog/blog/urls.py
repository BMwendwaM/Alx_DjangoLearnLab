from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

# URL patterns for post function

urlpatterns = [
    path("", views.home, name="home"),

    # Authentication URLs
    
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]