from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Api view for Book model

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer