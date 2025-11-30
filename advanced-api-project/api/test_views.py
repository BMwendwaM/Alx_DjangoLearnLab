from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Author, Book

# Tests for Book API endpoints


class BookAPITests(APITestCase):

    def setUp(self):
        # Create an author
        self.author = Author.objects.create(name="Bonnie")

        # Create a sample book
        self.book = Book.objects.create(
            title="Life",
            publication_year=1996,
            author=self.author
        )

    # List books
    def test_list_books(self):
        response = self.client.get(reverse("book-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # Filter books by author
    def test_filter_books_by_author(self):
        url = reverse("book-list") + f"?author={self.author.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # Search for books
    def test_search_books(self):
        url = reverse("book-list") + "?search=Sample"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # Order books
    def test_order_books(self):
        url = reverse("book-list") + "?ordering=title"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # ---------------- UNAUTH CREATE ----------------
    def test_create_book_unauthenticated(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(reverse("book-create"), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------- UNAUTH UPDATE ----------------
    def test_update_book_unauthenticated(self):
        data = {"title": "Updated"}
        response = self.client.patch(reverse("book-update", args=[self.book.id]), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ---------------- UNAUTH DELETE ----------------
    def test_delete_book_unauthenticated(self):
        response = self.client.delete(reverse("book-delete", args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
