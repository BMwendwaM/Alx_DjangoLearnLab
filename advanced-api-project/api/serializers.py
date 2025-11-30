from rest_framework import serializers
from datetime import date
from .models import Author, Book


# Serializers for Author and Book models.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


# Extra validation to ensure publication year is not in the future.

    def validate_publication_year(self, publication_year):
        current_year = date.today().year
        if publication_year > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")


class AuthorSerializer(serializers.ModelSerializer):

    # Nested serialization to include all books by the author.
    books = BookSerializer(many=True, read_only=True) 

    class Meta:
        model = Author
        fields = ['name', 'books']
