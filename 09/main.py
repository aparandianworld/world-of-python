#!/usr/bin/env python3


class Shape:
    width = 5
    height = 5
    printChar = "#"

    def printRow(self, i):
        raise NotImplementedError(
            "This method will be implemented by children classes extending this class."
        )

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)


class Triangle(Shape):
    def printRow(self, i):
        print(self.printChar * (i + 1))


def main():
    square = Square()
    square.print()
    print()

    triangle = Triangle()
    triangle.print()
    print()


if __name__ == "__main__":
    main()
