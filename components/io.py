import os


class ConsoleOutput:
    def print(self, msg: str):
        print(msg)

    def print_delimiter(self):
        print('=' * 50)

    def clear(self):
        command = 'clear'

        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'

        os.system(command)


class ConsoleInput:
    def input(self) -> str:
        return input()
