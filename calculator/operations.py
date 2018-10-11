def add(first, second):
    return first + second


def minus(first, second):
    return first - second


def multiplication(first, second):
    return first * second


def division(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        return 'Division by zero is invalid'


def mod(first, second):
    return first % second
