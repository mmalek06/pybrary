from argparse import ArgumentParser

from app.core.io import ConsoleInput, ConsoleOutput, read_library
from app.core.Library import Library
from app.core.enums import ActionType
from app.ui.UI import UI


parser = ArgumentParser()

parser.add_argument(
    '-f',
    '--file',
    default='data/default.tsv',
    dest='filename',
    help='pick a custom library filename',
    metavar='FILE')

args = parser.parse_args()
books = read_library(args.filename)
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
