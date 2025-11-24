#!/usr/bin/env python3


def is_prime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))


def all_primes_up_to(n):
    return [i for i in range(2, n + 1) if is_prime(i)]


def main():
    num = 100
    result = all_primes_up_to(num)

    print(f"Prime numbers up to {num}: {result}")


if __name__ == "__main__":
    main()