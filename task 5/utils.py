import argparse


class CharIterator(object):
    def __init__(self, data, start=0):
        self.data = data
        self.__count = start
        self.__limit = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.data[self.__count]
        self.__count += 1
        if self.__count == self.__limit:
            raise StopIteration
        return tmp


def createParser(parameters):
    parser = argparse.ArgumentParser()
    for p in parameters:
        parser.add_argument(p[0], p[1])
    return parser


def readFile(path_to_file, func):
    global file
    try:
        file = open(path_to_file, "r")
    except FileNotFoundError:
        exit(-1)

    temp_list = func(file)

    file.close()
    return temp_list


def write_file(data, path_to_file, func):
    f = open(path_to_file, 'w')
    func(f, data)
    f.close()
