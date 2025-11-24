#!/usr/bin/env python3


class NonIntArgumentException(Exception):
    def __init__(self, message):
        super().__init__(message)


def handleNonIntArguments(message="Non-integer argument provided"):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for item in args:
                if not isinstance(item, int):
                    raise NonIntArgumentException(message)
            for item in kwargs:
                if not isinstance(item, int):
                    raise NonIntArgumentException(message)
            return function(*args, **kwargs)

        return wrapper


@handleNonIntArguments
def sum(a, b, c):
    return a + b + c


def main():
    try:
        result = sum(1, 2, "a")
        print(f"Result: {result}")
    except NonIntArgumentException as e:
        print(f"Exception caught: {e}")


if __name__ == "__main__":
    main()
