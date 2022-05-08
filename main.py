from app.core.io import ConsoleInput, ConsoleOutput, read_library
from app.core.Library import Library
from app.core.enums import ActionType
from app.ui.UI import UI


books = read_library('data/default.tsv')
lib = Library(books)
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
