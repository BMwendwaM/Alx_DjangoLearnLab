from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path("books/", views.list_books, name="book_list"),
    path("library/", views.LibraryDetailView.as_view(), name="librarydetail"),
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    path('create_book/', views.create_book, name='create_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
    path('view_book/', views.view_book, name='view_book'),
]