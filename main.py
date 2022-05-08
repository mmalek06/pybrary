from app.core.io import ConsoleInput, ConsoleOutput
from app.core.Library import Library
from app.core.enums import ActionType
from app.ui.UI import UI
from app.core.models import Author, Book


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
    ),
    Book(
        '3456',
        'Wiedzmin',
        [Author('4', 'Andrzej Sapkowski')],
        1
    ),
    Book(
        '4567',
        'Starosc Aksolotla',
        [Author('5', 'Jacek Dukaj')],
        10
    ),
    Book(
        '5678',
        'Imperium Chmur',
        [Author('5', 'Jacek Dukaj')],
        5
    ),
    Book(
        '6789',
        'Through a Scanner Darkly',
        [Author('5', 'Philip K. Dick')],
        5
    )
])
cinput = ConsoleInput()
output = ConsoleOutput()
ui = UI(cinput, output)

ui.register_callback(lib.list_authors_books, ActionType.LIST_BOOKS)
ui.register_callback(lib.find_book, ActionType.FIND_BOOK)
ui.register_callback(lib.borrow_book, ActionType.BORROW_BOOK)
ui.register_callback(lib.return_book, ActionType.RETURN_BOOK)
ui.register_callback(lib.list_stock, ActionType.LIST_STOCK)

while ui.show():
    result = ui.action()

    if result == ActionType.EXIT:
        break
