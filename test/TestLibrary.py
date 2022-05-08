import unittest

from app.core.Library import Library
from app.core.errors import BookNotFoundError
from app.core.models import Book, Author


class TestLibrary(unittest.TestCase):
    def test_find_book_should_raise_error_when_no_books_found(self):
        library = Library([
            Book(
                '1234',
                'Wiedzmin',
                [Author('1', 'Andrzej Sapkowski')],
                1)])

        with self.assertRaises(BookNotFoundError):
            library.find_book('The Wienndzmin')

    def test_find_book_should_return_books_matching_the_criteria(self):
        author = Author('1', 'Andrzej Sapkowski')
        books = [
            Book(
                '1234',
                'Wiedzmin',
                [author],
                1),
            Book(
                '2345',
                'Wiedzmin 2',
                [author],
                1
            )]
        library = Library(books)

        found_books = library.find_book('wiedzmin')

        self.assertEqual(books, found_books)
