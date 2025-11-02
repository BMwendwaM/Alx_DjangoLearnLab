from django.contrib import admin

# Register your models here.
# Register Book model and custom admin panel

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register model + custom admin class

admin.site.register(Book, BookAdmin)