from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# LIST ALL BOOKS

def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)



# DETAILS FOR A BOOK IN SPECIFIC LIBRARY

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'books/library_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    library = self.get_object()
    context["books"] = library.books.all()
    return context