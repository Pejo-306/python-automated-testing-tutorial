def print_hello(name: str) -> None:
    print(f'Hello {name}!')


def throw_exception() -> None:
    raise Exception('Sample exception')


def divide_by_zero() -> float:
    return 1 / 0


def square(num: int) -> int:
    return num ** 2


def cube(num: int) -> int:
    return num ** 3
