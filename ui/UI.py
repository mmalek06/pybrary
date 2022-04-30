from core.io import ConsoleInput, ConsoleOutput
from core.enums import ActionType
from core.models import Book
from ui.validation import non_empty_validator


class UI:
    __input: ConsoleInput
    __output: ConsoleOutput
    __chosen_action: ActionType
    __callbacks: dict[ActionType, list]

    def __init__(self, cinput: ConsoleInput, output: ConsoleOutput):
        self.__input = cinput
        self.__output = output
        self.__chosen_action = ActionType.NONE
        self.__callbacks = dict()

    def register_callback(self, callback, action_type: ActionType):
        if action_type not in self.__callbacks:
            self.__callbacks[action_type] = []

        self.__callbacks[action_type].append(callback)

    def show(self) -> bool:
        self.__output.print_delimiter()
        self.__output.print('Welcome to our Library. What can we do for you?')
        self.__output.print('1 - list author\'s books')
        self.__output.print('2 - find a book')
        self.__output.print('3 - borrow a book')
        self.__output.print('4 - return a book')
        self.__output.print('5 - list stock')
        self.__output.print('6 - exit program')
        self.__output.print_delimiter()

        option = self.__input.input()

        if option is None or option.strip() == '':
            return True

        chosen_action = int(option)

        if chosen_action == 6:
            return False

        self.__output.clear()

        if chosen_action > 6 or chosen_action <= 0:
            self.__chosen_action = ActionType.NONE
        else:
            self.__chosen_action = ActionType(chosen_action)

        return True

    def action(self) -> ActionType:
        self.__output.print_delimiter()

        try:
            if self.__chosen_action is ActionType.LIST_BOOKS:
                self.__list_books()
            if self.__chosen_action is ActionType.FIND_BOOK:
                self.__find_book()
            if self.__chosen_action is ActionType.BORROW_BOOK:
                self.__borrow_book()
            if self.__chosen_action is ActionType.RETURN_BOOK:
                pass
            if self.__chosen_action is ActionType.LIST_STOCK:
                self.__list_stock()
        except Exception as exc:
            print(exc)

        self.__output.print_delimiter()

        return self.__chosen_action

    def __list_books(self):
        if ActionType.LIST_BOOKS not in self.__callbacks:
            return

        self.__output.print('Please type in the author\'s name: ')

        author_name = self.__input.input()

        non_empty_validator(author_name)

        for callback in self.__callbacks[ActionType.LIST_BOOKS]:
            result = callback(author_name)

            if result is None:
                continue
            if not isinstance(result, list):
                continue

            self.__output.print('')

            for book in result:
                self.__output.print(book)
            else:
                self.__output.print(f'No book found for the author {author_name}')

            self.__output.print('')

    def __find_book(self):
        if ActionType.FIND_BOOK not in self.__callbacks:
            return

        self.__output.print('Please type in the name of the book you\'re looking for: ')

        book_name = self.__input.input()

        non_empty_validator(book_name)

        for callback in self.__callbacks[ActionType.FIND_BOOK]:
            result = callback(book_name)

            if result is None:
                continue
            if isinstance(result, Book):
                self.__output.print(result)
            elif isinstance(result, list):
                for book in result:
                    self.__output.print(book)
                else:
                    self.__output.print(f'No book found for the search phrase: {book_name}')

    def __borrow_book(self):
        if ActionType.BORROW_BOOK not in self.__callbacks:
            return

        self.__output.print('Please type in the ISBN of the book you would like to borrow: ')

        isbn = self.__input.input()

        non_empty_validator(isbn)

        self.__output.print('')
        self.__output.print('Please type in the name of the person borrowing the book: ')

        user_name = self.__input.input()

        non_empty_validator(user_name)

        for callback in self.__callbacks[ActionType.BORROW_BOOK]:
            result = callback(isbn, user_name)

            if isinstance(result, Book):
                self.__output.print(f'{result} borrowed.')

    def __list_stock(self):
        if ActionType.LIST_STOCK not in self.__callbacks:
            return

        self.__output.print('Below you will find the list of books along with the')
        self.__output.print('number of copies available: ')

        for callback in self.__callbacks[ActionType.LIST_STOCK]:
            result = callback()

            if isinstance(result, list):
                for (book, stock) in result:
                    self.__output.print(f'{book} - {stock} copies left.')

