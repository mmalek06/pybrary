from components.io import ConsoleInput, ConsoleOutput
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

    def show(self) -> bool:
        self.__output.print('')
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

        if chosen_action is 5:
            return False

        self.__output.clear()

        if chosen_action > 5 or chosen_action <= 0:
            self.__chosen_action = ActionType.NONE
        else:
            self.__chosen_action = ActionType(chosen_action)

        return True

    def action(self):
        if self.__chosen_action is ActionType.NONE:
            return
        if self.__chosen_action is ActionType.LIST_BOOKS:
            self.__list_books()
        if self.__chosen_action is ActionType.FIND_BOOK:
            pass
        if self.__chosen_action is ActionType.BORROW_BOOK:
            pass
        if self.__chosen_action is ActionType.RETURN_BOOK:
            pass
        if self.__chosen_action is ActionType.EXIT:
            pass

    def __list_books(self):
        self.__output.print_delimiter()
        self.__output.print('Please type in the author\'s name: ')

        author_name = self.__input.input()

        if ActionType.LIST_BOOKS in self.__callbacks:
            for callback in self.__callbacks[ActionType.LIST_BOOKS]:
                result = callback(author_name)

                if result is None:
                    continue
                if not isinstance(result, list):
                    continue

                self.__output.print('')

                for book in result:
                    self.__output.print(f'Book: {book.title}, ISBN: {book.isbn}')

                self.__output.print('')

        self.__output.print_delimiter()
