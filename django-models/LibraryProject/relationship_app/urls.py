from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("books/", list_books, name="book_list"),
    path("library/", LibraryDetailView.as_view(), name="librarydetail"),
]