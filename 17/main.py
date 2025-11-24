#!/usr/bin/env python3

import csv
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "--input", "-i", required=True, help="Input CSV file to process"
    )
    parser.add_argument(
        "--output",
        "-o",
        required=True,
        help="Output processed CSV file containing only rows with employee_id and email",
    )
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    try:
        with open(input_file, "r") as fh:
            reader = list(csv.reader(fh))
            with open(output_file, "w", newline="") as ofh:
                writer = csv.writer(ofh)
                for row in reader[1:]:
                    if len(row) > 4:
                        employee_id = row[0]
                        email = row[4]
                        writer.writerow([employee_id, email])

    except FileNotFoundError as e:
        print(f"Input file {input_file} not found: {e}")

    except IOError as e:
        print(f"An I/O error occured: ", {e})

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
