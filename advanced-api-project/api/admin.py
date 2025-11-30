from django.contrib import admin
from .models import Author, Book

# Register Book and Author models to appear in the admin interface.

admin.site.register(Author)
admin.site.register(Book)