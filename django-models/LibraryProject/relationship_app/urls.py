from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView

# login

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path


urlpatterns = [
    path("books/", list_books, name="book_list"),
    path("library/", LibraryDetailView.as_view(), name="librarydetail"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
