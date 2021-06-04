import argparse
import re
import sys


def task(path_to_file, path_to_output, file=None):
    file
    try:
        file = open(path_to_file, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Please enter the correct file name.")
        return

    temp_list = []
    for line in file.readlines():
        temp_list = re.split(r'[*\n*\W*\s]', line.strip())

    file.close()

    changed_list = find_words(temp_list)

    if path_to_output == 'None':
        path_to_output = 'default.txt'

    output_file = open(path_to_output, "w", encoding="utf-8")
    for word in changed_list:
        output_file.write(str(word) + '\n')

    output_file.close()


def find_words(text):
    temp_list = []
    for word in text:
        if check_word(word):
            temp_list.append(word)
    return temp_list


def check_word(word):
    count = {}
    for s in word:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] >= 3:
            return True

    return False


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
