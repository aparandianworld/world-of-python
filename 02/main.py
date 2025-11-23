#!/usr/bin/env python3

# Hex 1A3 -> decimal 419
# 3 * 16^0 = 3
# A (10) * 16^1 = 160
# 1 * 16^2 = 256
# Total: 3 + 160 + 256 = 419


def manual_hex_to_decimal(hex_str):
    decimal = 0
    power = 0

    for current_char in reversed(hex_str):
        if "0" <= current_char <= "9":
            value = ord(current_char) - ord("0")
        elif "A" <= current_char <= "F":
            value = ord(current_char) - ord("A") + 10

        decimal += value * (16**power)
        power += 1

    return decimal


def hex_to_decimal(hex_str):
    return int(hex_str, 16)


def main():
    print(f"Enter a Hex number: ")
    hex_input = input().upper().strip()
    decimal_input = hex_to_decimal(hex_input)
    manual_decimal_input = manual_hex_to_decimal(hex_input)
    print(
        f"Hex {hex_input} = Decimal {decimal_input} | Decimal (manual): {manual_decimal_input}"
    )


if __name__ == "__main__":
    main()
