import argparse
import re
import sys
from segment import Segment


def task(segments):
    if len(segments) == 1:
        return segments[0]
    elif len(segments) == 0:
        raise Exception("Исходные данные неверны")

    s = sorted(segments, reverse=True, key=lambda segment: segment.size)
    intersection = None
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i].end >= s[j].start and s[i].start <= s[j].end:
                tmp = merge(s[i], s[j])
                if intersection is None:
                    intersection = tmp
                elif intersection.size <= tmp.size:
                    intersection = tmp
    if intersection is not None:
        return intersection
    return s[0], s[1]


def merge(seg1, seg2):
    return Segment(min(seg1.start, seg2.start), max(seg1.end, seg2.end))


def write_file(data, path_to_file):
    f = open(path_to_file, 'w')
    if isinstance(data, tuple):
        for i in data:
            f.write(str(i) + "\n")
    elif isinstance(data, Segment):
        f.write(str(data))


def readFile(path_to_file):
    try:
        file = open(path_to_file, "r")
    except FileNotFoundError:
        print("Please enter the correct file name:")
        readFile(input())

    temp_list = []
    for line in file.readlines():
        if line != '\n':
            temp_list.append(re.split(r'[*\n*\s]', line.strip()))

    file.close()
    return temp_list  # возвращаем список строк считанных из файла


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i')
    parser.add_argument('--output', '-o')
    return parser


def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    listOfPoints = readFile(str(namespace.input))  # читаем данные из файла
    segments = []
    for coords in listOfPoints:  # создаем отрезки из входных данных
        segments.append(Segment(float(coords[0]), float(coords[1])))

    result = task(segments)
    write_file(result, str(namespace.output))


if __name__ == '__main__':
    main()
