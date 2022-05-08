import csv
import os

from app.core.models import Book, Author


class ConsoleOutput:
    def print(self, msg):
        print(msg)

    def print_delimiter(self):
        print('=' * 50)

    def clear(self):
        command = 'clear'

        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'

        os.system(command)


class ConsoleInput:
    def input(self) -> str:
        return input()


def read_library(file_path: str) -> list[Book]:
    result = []

    with open(file_path) as file:
        tsv_file = csv.reader(file, delimiter='\t')

        for line in tsv_file:
            isbn = line[0]
            title = line[1]
            authors = list(map(lambda x: _get_author(x), line[2].split(';')))
            stock = int(line[3])

            result.append(Book(isbn, title, authors, stock))

    return result


def _get_author(author_data: str) -> Author:
    parts = author_data.split(' ', 1)

    return Author(parts[0], parts[1])
