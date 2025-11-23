from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Api view for Book model

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# New ViewSet for all CRUD operations

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer