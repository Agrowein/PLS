import argparse
import re
import sys


def task(path_to_file, path_to_output, n, file=None):
    file
    try:
        file = open(path_to_file, "r")
    except FileNotFoundError:
        print("Please enter the correct file name:")
        task(input(), path_to_output, n)

    temp_list = []
    for line in file.readlines():
        temp_list.append(re.split(r'[*\n*\s]', line.strip()))

    file.close()

    if n == 'None':
        print("Please enter the value of shift:")
        n = input()

    n = int(n)

    transformer_list = move_diagonal(temp_list, n)

    if path_to_output == 'None':
        print("Please enter the correct output file name:")
        path_to_output = input()

    output_file = open(path_to_output, "w")
    for line in transformer_list:
        output_file.write(str(line) + "\n")

    output_file.close()


def move_diagonal(array, n):
    return_list = []

    for line in array:
        return_list.append(shift(line, n))

    return return_list


def shift(array, n):
    return array[-n:] + array[:-n]


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i')
    parser.add_argument('--output', '-o')
    parser.add_argument('--shift', '-s')

    return parser


def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    task(str(namespace.input), str(namespace.output), str(namespace.shift))


if __name__ == '__main__':
    main()
