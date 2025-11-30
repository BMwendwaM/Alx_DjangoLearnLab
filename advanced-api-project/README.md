This project implements a structured API for managing books using Django REST Framework’s generic views.
The system includes dedicated views for listing all books, retrieving a single book, creating new entries, updating existing records and deleting books. 
Each view is mapped to intuitive URL patterns that make the API easy to navigate and interact with.
To maintain secure and predictable behavior, permission classes are applied across the views so that only authenticated users can create, update or delete books, while read-only access is available to all for listing and viewing details.
The API is tested through manual requests using Postman tool.




** Book List API with Filtering and Search **

GET /api/books/
Retrieve a list of books.

** Examples **

-- Filter by publication year --

GET /api/books/?publication_year=1996
Returns all books published in 1996.

-- Search by title or author name --

GET /api/books/?search=King
Returns all books where the title or author name contains "King".
