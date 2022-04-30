import typing

from .errors import BookBorrowedError, BookNotFoundError
from .models import Author, Book

from .functions import lev_dist


class Library:
    __borrowed_books: dict[str, list[str]]
    __books: list[Book]
    __book_search_sensitivity: int = 10
    __author_search_sensitivity: int = 2

    def __init__(self, books: list[Book]):
        self.__borrowed_books = dict()
        self.__books = books

    def list_authors_books(self, maybe_author_name: str) -> list[Book]:
        found_books = []

        for book in self.__books:
            for author in book.authors:
                distance = lev_dist(author.name.lower(), maybe_author_name.lower())

                if distance > self.__author_search_sensitivity:
                    continue

                found_books.append(book)

                break

        return found_books

    def find_book(self, maybe_title: str) -> typing.List[Book] | Book:
        candidates = []

        for book in self.__books:
            distance = lev_dist(book.title.lower(), maybe_title.lower())

            if distance > self.__book_search_sensitivity:
                continue

            candidates.append(book)

        if len(candidates) == 0:
            raise BookNotFoundError(f'''A book entitled {maybe_title} not found and there are no similarly entitled books in the library.''')
        if candidates[0].title is maybe_title:
            return candidates[0]

        return candidates

    def borrow_book(self, isbn: str, user_name: str) -> Book:
        found_book = self.__lookup_book(isbn)

        if found_book.isbn not in self.__borrowed_books:
            self.__borrowed_books[found_book.isbn] = list()

        self.__borrowed_books[found_book.isbn].append(user_name)

        return found_book

    def list_stock(self) -> list[(Book, int)]:
        stock = []

        for key in self.__borrowed_books:
            book = self.__lookup_book(key)

            stock.append((book, book.stock - len(self.__borrowed_books[key])))

        return stock

    def __lookup_book(self, isbn) -> Book:
        for book in self.__books:
            if book.isbn != isbn:
                continue
            if book.isbn in self.__borrowed_books and len(self.__borrowed_books[book.isbn]) >= book.stock:
                raise BookBorrowedError(f'Book {book.title} has already been borrowed by someone else.')

            return book

        raise BookNotFoundError(f'A book with isbn = {isbn} not found.')
