from relationship_app.models import Author, Book, Library, Librarian

# BOOK BY AUTHOR
author_name = "Orwell"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)
for book in books:
    print(book.title)


# LIST ALL BOOKS IN A LIBRARY
library_name = "Library"
library = Library.objects.get(name=library_name)
books = library.books.all()
for book in books:
    print(book)



# RETRIEVE A LIBRARIAN
librarian = Librarian.objects.get(library="LIBRARY")
print(librarian.name)