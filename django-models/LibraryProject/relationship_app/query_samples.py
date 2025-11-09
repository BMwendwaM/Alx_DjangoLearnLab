from relationship_app.models import Author, Book, Library, Librarian

# BOOK BY AUTHOR
author = Author.objects.get(name="Orwell")
books = Book.objects.filter(author=author)


# LIST ALL BOOKS IN A LIBRARY
library = Library.objects.get(name=library_name)
books = library.books.all()
for i in books:
    print(i)



# RETRIEVE A LIBRARIAN
library = Library.objects.get(name="LIBRARY")
librarian = library.librarian
print(librarian.name)