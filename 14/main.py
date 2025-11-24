#!/usr/bin/env python3


def main():
    try:
        with open("./zen.txt", "r") as fh:
            for line in fh.readlines():
                print(line.strip())

        with open("./out.txt", "w") as fh:
            content = "Now is better than never..."
            fh.write(content)

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
