import typing

from functools import lru_cache

from models import Author, User, Book
from errors import BookBorrowedError, BookNotFoundError


class Library:
    borrowed_books = dict[Book, list[User]]()

    __books: list[Book]
    __book_search_sensitivity: int = 10
    __author_search_sensitivity: int = 2

    def __init__(self, books_with_authors: list[Book]):
        self.__books = books_with_authors

    def list_authors_books(self, maybe_author_name: str):
        found_books = []

        for book in self.__books:
            for author in book.authors:
                distance = Library.__lev_dist(author.name, maybe_author_name)

                if distance > self.__author_search_sensitivity:
                    continue

                found_books.append(book)

                break

        return found_books

    def find_book(self, maybe_title: str) -> typing.List[Book] | Book:
        candidates = []

        for book in self.__books:
            distance = Library.__lev_dist(book.title.lower(), maybe_title.lower())

            if distance > self.__book_search_sensitivity:
                continue

            candidates.append(book)

        if len(candidates) == 0:
            raise BookNotFoundError(f'''A book entitled {maybe_title} not found and there are no similarly entitled books in the library.''')
        if candidates[0].title is maybe_title:
            return candidates[0]

        return candidates

    def rent_book(self, isbn: str, user: User) -> Book:
        found_book = self.__find_book(isbn)

        if found_book not in self.borrowed_books:
            self.borrowed_books[found_book] = list()

        self.borrowed_books[found_book].append(user)

        return found_book

    def __find_book(self, isbn) -> Book:
        for book in self.__books:
            if book.isbn is not isbn:
                continue
            if book in self.borrowed_books and len(self.borrowed_books[book]) >= book.stock:
                raise BookBorrowedError(f'Book {book.title} has already been borrowed by someone else.')

            return book

        raise BookNotFoundError(f'A book with isbn = {isbn} not found.')

    @staticmethod
    def __lev_dist(a: str, b: str) -> int:
        '''
        This function will calculate the levenshtein distance between two input
        strings a and b

        params:
            a (String) : The first string you want to compare
            b (String) : The second string you want to compare

        returns:
            This function will return the distnace between string a and b.

        example:
            a = 'stamp'
            b = 'stomp'
            lev_dist(a,b)
            >> 1.0
        '''

        @lru_cache(None)  # for memorization
        def min_dist(s1: int, s2: int) -> int:
            if s1 == len(a) or s2 == len(b):
                return len(a) - s1 + len(b) - s2

            # no change required
            if a[s1] == b[s2]:
                return min_dist(s1 + 1, s2 + 1)

            return 1 + min(
                min_dist(s1, s2 + 1),  # insert character
                min_dist(s1 + 1, s2),  # delete character
                min_dist(s1 + 1, s2 + 1),  # replace character
            )

        return min_dist(0, 0)
