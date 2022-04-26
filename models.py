from typing import NamedTuple


class Author(NamedTuple):
    identifier: str
    name: str


class Book(NamedTuple):
    isbn: str
    title: str
    authors: list[Author]
    stock: int


class User(NamedTuple):
    identifier: str
    name: str
