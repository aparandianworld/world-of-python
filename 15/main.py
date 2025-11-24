#!/usr/env/bin python3

import csv


def main():
    try:
        with open("./employees.csv", "r") as fh:
            reader = csv.reader(fh)
            for row in reader:
                print(row)

        print(f"Remove header ---")

        with open("./employees.csv", "r") as fh:
            reader = list(csv.reader(fh))
            for row in reader[1:]:
                print(row)

        print(f"Read as dictionary ---")

        with open("./employees.csv", "r") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                print(row)

        print(f"Write employee_id and first_name to new file ---")

        with open("./out.csv", "w") as wh:
            writer = csv.writer(wh)
            with open("./employees.csv", "r") as rh:
                reader = csv.DictReader(rh)
                for row in reader:
                    writer.writerow([row["employee_id"], row["first_name"]])

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
