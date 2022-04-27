from typing import NamedTuple


class Author(NamedTuple):
    identifier: str
    name: str


class Book(NamedTuple):
    isbn: str
    title: str
    authors: list[Author]
    stock: int

    def __str__(self):
        authors = ', '.join(map(lambda author: author.name, self.authors))

        return f'Book: {self.title}, ISBN: {self.isbn}, written by: {authors}'


class User(NamedTuple):
    identifier: str
    name: str
