import os
import unittest

from app.core.io import read_library
from app.core.models import Book, Author


class TestReadLibrary(unittest.TestCase):
    def test_file(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = f'{dir_path}/data/test_default.tsv'
        result = read_library(file_path)

        self.assertEqual(
            result,
            [
                Book(
                    '1234',
                    'Mathematics for Machine Learning',
                    [
                        Author('1', 'Marc Peter Deisenroth'),
                        Author('2', 'A. Aldo Faisal'),
                        Author('3', 'Cheng Soon Ong')
                    ],
                    2),
                Book(
                    '2345',
                    'Trylogia Husycka',
                    [
                        Author('4', 'Andrzej Sapkowski')
                    ],
                    3)
            ])
