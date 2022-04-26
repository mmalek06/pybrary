from components.functions import clear_console
from components.ui.enums import ActionType
from models import Book


class UI:
    __chosen_action: ActionType
    __callbacks: dict[ActionType, list]

    def __init__(self):
        self.__chosen_action = ActionType.NONE
        self.__callbacks = dict()

    def show(self) -> bool:
        print('')
        UI.__print_delimiter()
        print('Welcome to our Library. What can we do for you?')
        print('1 - list author\'s books')
        print('2 - find a book')
        print('3 - borrow a book')
        print('4 - return a book')
        print('5 - exit program')
        UI.__print_delimiter()
        print('')

        chosen_action = int(input())

        if chosen_action is 5:
            return False

        clear_console()

        if chosen_action > 5 or chosen_action <= 0:
            self.__chosen_action = ActionType.NONE
        else:
            self.__chosen_action = ActionType(chosen_action)

        return True

    def action(self):
        if self.__chosen_action is ActionType.NONE:
            return
        if self.__chosen_action is ActionType.LIST_BOOKS:
            pass
        if self.__chosen_action is ActionType.FIND_BOOK:
            pass
        if self.__chosen_action is ActionType.BORROW_BOOK:
            pass
        if self.__chosen_action is ActionType.RETURN_BOOK:
            pass
        if self.__chosen_action is ActionType.EXIT:
            pass

    def __list_books(self):
        UI.__print_delimiter()
        print('Please type in the author\'s name: ')

        author_name = input()

        if ActionType.LIST_BOOKS in self.__callbacks:
            for callback in self.__callbacks[ActionType.LIST_BOOKS]:
                result = callback(author_name)

                if result is None:
                    continue

                if result is list[Book]:
                    for book in result:
                        print(f'Book: {book.title}, ISBN: {book.isbn}')

        UI.__print_delimiter()

    @staticmethod
    def __print_delimiter():
        print('=' * 50)
