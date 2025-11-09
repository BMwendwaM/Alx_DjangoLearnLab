
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
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
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    
    def register(request):
       view = RegisterView.as_view()
       return view(request)
    


# USER MODEL ROLE_BASED VIEWS
# Define roles
ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
]


# Admin view
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(lambda u: hasattr(u, 'userprofile') and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



# PERMISSION VIEWS

@permission_required("relationship_app.can_add_book")
def add_book(request):
   if request.method == 'POST':
      return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request):
   return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request):
   return render(request, 'relationship_app/delete_book.html')