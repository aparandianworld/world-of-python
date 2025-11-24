#!/usr/bin/env python3


def introduce(name, age, *args, **kwargs):
    print(f"Hello, I'm {name}, {age} years old.")
    if args:
        print(f"Additional (positional) info: {args}")
    if kwargs:
        print(f"Extra keyword or named details: {kwargs}")


def main():
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]

    # sort by age
    sorted_users_by_age = sorted(users, key=lambda user: user["age"])
    print("Sorted users by age:")
    print(sorted_users_by_age)

    # sort by name
    sorted_users_by_name = sorted(users, key=lambda user: user["name"])
    print("Sorted users by name:")
    print(sorted_users_by_name)

    introduce("Alice", 28, "Software Engineer", "London", "Likes hiking")
    print("---")
    introduce("Aaron", 34, job="Software Engineer", city="Paris", hobby="Swimming")


if __name__ == "__main__":
    main()
