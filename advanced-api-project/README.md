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



** TESTS FOR API ENDPOINTS **

This project includes basic tests to confirm that the Book API endpoints work correctly. The tests check essential operations such as listing books, filtering, and searching, as well as ensuring that unauthorized users receive the proper error response when trying to access protected endpoints. These tests use Django REST Framework’s built-in APIClient and a temporary test database created automatically during testing.

To run the tests, use "python manage.py test". The tests validate that each endpoint returns the correct status code and expected data. Simple examples, such as checking that the book list returns one sample book or that search results match the query, help verify that the API behaves correctly and meets the project requirements.
