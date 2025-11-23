from django.contrib import admin
from .models import Book

# Book model registration

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
