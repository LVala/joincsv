from typing import Iterable

import sys
import csv
import os

LEFT = 1
RIGHT = 2
INNER = 3

def gen_header(left_csv_path: str, right_csv_path: str, col_name: str) -> list[str]:
    """
    Returns list of fieldnames for the header of new, merged csv file
    """
    try:
        with open(left_csv_path, "r") as left_file, open(right_csv_path, "r") as right_file:
            left_reader = csv.reader(left_file)
            right_reader = csv.reader(right_file)
            
            left_header = next(left_reader)  # first line of the file is a header
            right_header = next(right_reader)

            if col_name not in left_header or col_name not in right_header:
                print("Error: join column absent in one of the files")
                exit(1)

            header = []
            right_header.remove(col_name)
            header.extend(left_header)
            header.extend(right_header)
            return header

    except IOError as e:  # in case the files does not exist or user lacks permisions
        print(f"Error while trying to read one of the files: {e.strerror}")
        exit(1)

def read_csv(path: str) -> Iterable[dict[str,str]]:
    """
    Returns a generator which yields dict representing
    next line of the csv file. This being a generator prevents from
    memory overflows, as it is not loaded to memory in its entirety
    """
    try:
        with open(path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                yield row

    except IOError as e:
        print(f"Error with reading {path}: {e.strerror}")
        exit(1)

def join_csv(left_csv_path: str, right_csv_path: str, col_name: str, mode: int) -> None:
    """
    Creates a new csv file which consists of rows from @left_csv_path and @right_csv_path
    merged based on choosen @mode, more information in README.md
    """
    header = gen_header(left_csv_path, right_csv_path, col_name)

    # generate new filename, makes sure no file is overwritten
    i = 1
    new_name = "joined_" + str(i) + ".csv"
    while os.path.exists(new_name):
        i += 1
        new_name = "joined_" + str(i) + ".csv"
    
    try:
        with open(new_name, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=header, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            
            # iterates over file A and for every element searches for matching elements in file B
            if mode in {INNER, LEFT}:
                left_csv = read_csv(left_csv_path)
                for left_row in left_csv:
                    right_csv = read_csv(right_csv_path)
                    was_written = False
                    for right_row in right_csv:
                        if right_row[col_name] == left_row[col_name]:
                            writer.writerow(left_row | right_row)
                            was_written = True
                    if mode == LEFT and not was_written:
                        writer.writerow(left_row)

            elif mode == RIGHT:
                right_csv = read_csv(right_csv_path)
                for right_row in right_csv:
                    left_csv = read_csv(left_csv_path)
                    was_written = False
                    for left_row in left_csv:
                        if right_row[col_name] == left_row[col_name]:
                            writer.writerow(left_row | right_row)
                            was_written = True
                    if not was_written:
                        writer.writerow(right_row)

    except IOError as e:
        print(f"Error with writing to new file: {e.strerror}")
        exit(1)

def main() -> int:
    if len(sys.argv) != 5 and len(sys.argv) != 4:
        print("Error: invalid number of arguments, expected 3")
        exit(1)

    if len(sys.argv) == 4:
        join_type = INNER
    elif sys.argv[4] == "left":
        join_type = LEFT
    elif sys.argv[4] == "right":
        join_type = RIGHT
    elif sys.argv[4] == "inner":
        join_type = INNER
    else:
        print("Error: invalid join type, expected one of {left, right, inner}")
        exit(1)

    left_path = os.path.normpath(sys.argv[1])
    right_path = os.path.normpath(sys.argv[2])

    join_csv(left_path, right_path, sys.argv[3], join_type)

    return 0;
