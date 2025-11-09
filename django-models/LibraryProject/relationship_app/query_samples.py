from relationship_app.models import Author, Book, Library, Librarian

# BOOK BY AUTHOR
author = Author.objects.get(name="Orwell")
books = Book.objects.filter(author=author)


# LIST ALL BOOKS IN A LIBRARY
library = Library.objects.all()
for i in library:
    print(i)


# RETRIEVE A LIBRARIAN
library = Library.objects.get(name="LIBRARY")
librarian = Library.Librarian
print(Librarian.name)