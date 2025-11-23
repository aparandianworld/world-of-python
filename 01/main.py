#!/usr/bin/env python3


def factorial_iterative(number):
    if type(number) != int:
        return None
    if number < 0:
        return None

    fact = 1
    counter = 1
    while counter <= number:
        fact *= counter
        counter += 1
    return fact


def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial_recursive(number - 1)


def main():
    print(f"Enter a integer number: ")

    number = int(input())
    if number >= 0:
        result_i = factorial_iterative(number)
        result_r = factorial_recursive(number)
        print(f"The iterative factorial of {number} is: {result_i}")
        print(f"The recursive factorial of {number} is: {result_r}")
    else:
        print(f"Error - Factorial is not defined for negative numbers.")


if __name__ == "__main__":
    main()
