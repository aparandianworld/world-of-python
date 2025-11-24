#!/usr/bin/env python3


class UniqueList(list):
    def __init__(self):
        super().__init__()  # call parent class init
        self.name = "Aaron's UniqueList Class"
        self.description = (
            "Aaron's implementation of a unique list that only stores unique elements"
        )

    def append(self, item):
        if item not in self:
            super().append(item)


def main():
    unique_list = UniqueList()
    unique_list.append(1)
    unique_list.append(2)
    unique_list.append(3)
    unique_list.append(1)
    unique_list.append(4)
    unique_list.append(2)

    print(f"Unique list: {unique_list}")
    print(f"Length: {len(unique_list)}")
    print(f"Name: {unique_list.name}")
    print(f"Description: {unique_list.description}")


if __name__ == "__main__":
    main()
