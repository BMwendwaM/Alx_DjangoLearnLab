from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register Book model and custom admin panel

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register model + custom admin class

admin.site.register(Book, BookAdmin)



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {'fields': ('date_of_birth', 'profile_photo')}),
    )