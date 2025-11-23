from django.urls import path
from .views import BookList

# Maps to the BookList view

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]