from enum import Enum


class ActionType(Enum):
    NONE = 0
    LIST_BOOKS = 1
    FIND_BOOK = 2
    BORROW_BOOK = 3
    RETURN_BOOK = 4
    EXIT = 5
