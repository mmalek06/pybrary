class EmptyInputError(Exception):
    pass


def non_empty_validator(data: str):
    if data.strip() == '':
        raise EmptyInputError('No data was passed, try again.')
