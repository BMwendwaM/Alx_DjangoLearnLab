from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

# PERMISSION VIEWS

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
   if request.method == 'POST':
      return render(request, 'bookshelf/add_book.html')

@permission_required("bookshelf.can_view", raise_exception=True)
def view_book(request):
   return render(request, 'bookshelf/change_book.html')

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request):
   return render(request, 'bookshelf/delete_book.html')

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request):
   return render(request, 'bookshelf/edit_book.html')