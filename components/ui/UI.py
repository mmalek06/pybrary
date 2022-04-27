from components.io import ConsoleInput, ConsoleOutput
from components.ui.decorators import with_delimiters
from components.ui.enums import ActionType
from models import Book


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

    @with_delimiters
    def show(self) -> bool:
        self.__output.print_delimiter()
        self.__output.print('Welcome to our Library. What can we do for you?')
        self.__output.print('1 - list author\'s books')
        self.__output.print('2 - find a book')
        self.__output.print('3 - borrow a book')
        self.__output.print('4 - return a book')
        self.__output.print('5 - exit program')
        self.__output.print_delimiter()
        self.__output.print('')

        chosen_action = int(self.__input.input())

        if chosen_action == 5:
            return False

        self.__output.clear()

        if chosen_action > 5 or chosen_action <= 0:
            self.__chosen_action = ActionType.NONE
        else:
            self.__chosen_action = ActionType(chosen_action)

        return True

    @with_delimiters
    def action(self) -> ActionType:
        if self.__chosen_action is ActionType.LIST_BOOKS:
            self.__list_books()
        if self.__chosen_action is ActionType.FIND_BOOK:
            self.__find_book()
        if self.__chosen_action is ActionType.BORROW_BOOK:
            pass
        if self.__chosen_action is ActionType.RETURN_BOOK:
            pass

        return self.__chosen_action

    def __list_books(self):
        self.__output.print('Please type in the author\'s name: ')

        author_name = self.__input.input()

        if ActionType.LIST_BOOKS not in self.__callbacks:
            self.__output.print_delimiter()

            return

        for callback in self.__callbacks[ActionType.LIST_BOOKS]:
            result = callback(author_name)

            if result is None:
                continue
            if not isinstance(result, list):
                continue

            self.__output.print('')

            for book in result:
                self.__output.print(book)

            self.__output.print('')

    def __find_book(self):
        self.__output.print('Please type in the name of the book you\'re looking for: ')

        book_name = self.__input.input()

        if ActionType.FIND_BOOK not in self.__callbacks:
            self.__output.print_delimiter()

            return

        for callback in self.__callbacks[ActionType.FIND_BOOK]:
            result = callback(book_name)

            if result is None:
                continue
            if isinstance(result, Book):
                self.__output.print(result)
            elif isinstance(result, list):
                for book in result:
                    self.__output.print(book)
