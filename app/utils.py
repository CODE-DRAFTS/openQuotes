from random import randrange


def random_number(numA: int , numB: int):
    return randrange(numA, numB)


def to_integer(input: str):
    try:
        return int(input)
    except Exception as error:
        return None