from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.list_books, name="book_list"),
    path("library/", views.LibraryDetailView.as_view(), name="librarydetail"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]
