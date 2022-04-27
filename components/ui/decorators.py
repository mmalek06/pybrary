def with_delimiters(func):
    def decorator(self, *args, **kwargs):
        self.__output.print_delimiter()
        func(*args, **kwargs)
        self.__output.print_delimiter()

    return decorator
