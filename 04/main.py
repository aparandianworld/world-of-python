#!/usr/bin/env python3

"""
Run-length encoding in python
Encode example: input "aaabbbcccaaa" should produce [('a', 3), ('b', 3), ('c', 3), ('a', 3)]
Decode example: input [('a', 3), ('b', 3), ('c', 3), ('a', 3)] should produce "aaabbbcccaaa"
"""


def encode_string(text: str) -> list[tuple[str, int]]:
    if not text:
        return []

    result = []
    current_char = text[0]
    count = 1

    for char in text[1:]:  # skipped first character here
        if char == current_char:
            count += 1
        else:
            result.append((current_char, count))
            current_char = char
            count = 1

    result.append((current_char, count))
    return result


def decode_string(encoded: list[tuple[str, int]]) -> str:
    result = ""

    for char, count in encoded:
        result += char * count
    return result


def main():
    encoding_test_cases = ["aaabbbcccaaa", "aabbcc", "aaaaaaa"]

    for test in encoding_test_cases:
        encoded = encode_string(test)
        print(f"Input: {test} -> Encoded: {encoded}")

    decoding_test_cases = [
        [("a", 3), ("b", 3), ("c", 3), ("a", 3)],
        [("a", 2), ("b", 2), ("c", 2)],
    ]
    for test in decoding_test_cases:
        decoded = decode_string(test)
        print(f"Encoded: {test} -> Decoded: {decoded}")


if __name__ == "__main__":
    main()
