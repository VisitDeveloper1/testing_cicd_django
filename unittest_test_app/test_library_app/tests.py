from django.test import TestCase
from django.urls import reverse
from .models import Book
from .forms import BookForm

class BookModelTest(TestCase):
    def setUp(self):
        # Set up data for the test
        self.book = Book.objects.create(
            title="Test-Driven Development",
            author="Kent Beck",
            published_date="2024-01-01"
        )

    def test_book_creation(self):
        """Test if the Book instance is created correctly."""
        self.assertEqual(self.book.title, "Test-Driven Development")
        self.assertEqual(self.book.author, "Kent Beck")
        self.assertEqual(str(self.book), "Test-Driven Development")

class BookViewTest(TestCase):
    def setUp(self):
        # Create test data
        Book.objects.create(title="Book 1", author="Author 1", published_date="2024-01-01")
        Book.objects.create(title="Book 2", author="Author 2", published_date="2024-02-01")

    def test_book_list_view(self):
        """Test the book list view."""
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("books", response.json())
        self.assertEqual(len(response.json()["books"]), 2)

class BookFormTest(TestCase):
    def test_valid_form(self):
        """Test if the form is valid with correct data."""
        form_data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "published_date": "2024-03-01"
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if the form is invalid with missing data."""
        form_data = {"title": "Clean Code"}
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())