#!/usr/bin/env python3

import sys
import timeit


def main():
    x = list(range(1000))
    y = tuple(range(1000))

    # memory comparison
    print(f"List size: {sys.getsizeof(x)} bytes")
    print(f"Tuple size: {sys.getsizeof(y)} bytes")

    # performance comparison
    list_time = timeit.timeit("list(range(1000))", globals=globals(), number=1000)
    tuple_time = timeit.timeit("tuple(range(1000))", globals=globals(), number=1000)

    print(f"List creation time: {list_time:.4f} seconds")
    print(f"Tuple creation time: {tuple_time:.4f} seconds")


if __name__ == "__main__":
    main()
