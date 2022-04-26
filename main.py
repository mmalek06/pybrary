from components.Library import Library
from models import Author, Book


lib = Library([
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
        [Author('4', 'Andrzej Sapkowski')],
        3
    )
])
