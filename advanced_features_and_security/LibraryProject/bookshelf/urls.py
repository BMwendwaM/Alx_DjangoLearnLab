from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # Book list and CRUD
    path("books/", views.book_list, name="book_list"),
    path("create_book/", views.create_book, name="create_book"),
    path("view_book/<int:book_id>/", views.view_book, name="view_book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete_book"),

    # Authentication
    path("login/", LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),

    # Placeholder for future views
    # path("register/", views.register, name="register"),
    # path("admin-view/", views.admin_view, name="admin_view"),
    # path("librarian-view/", views.librarian_view, name="librarian_view"),
    # path("member-view/", views.member_view, name="member_view"),
    # path("library/", views.LibraryDetailView.as_view(), name="librarydetail"),
]
