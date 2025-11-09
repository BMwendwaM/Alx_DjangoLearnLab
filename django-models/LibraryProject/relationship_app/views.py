#books

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# registration 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# login

from django.contrib.auth import login

# LIST ALL BOOKS

def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)



# DETAILS FOR A BOOK IN SPECIFIC LIBRARY

class LibraryDetailView(DetailView):
  model = Library
  template_name = 'relationship_app/library_detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    library = self.get_object()
    context["books"] = library.books.all()
    return context




# class based view for registration

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
