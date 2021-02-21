import argparse
import sys

def transformList(list1, list2):
    currList = list()
    for i in list1:
        for j in range(list2.count(i)):
            currList.append(i)

    return currList


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file1', '-f1')
    parser.add_argument('--file2', '-f2')

    return parser

def task1(input1, input2):
    print("\n##########################################################3\nTask1")
    file1 = open(input1)
    file2 = open(input2)
    list1 = file1.readline().split()
    list2 = file2.readline().split()

    file1.close()
    file2.close()

    transformList(list1, list2)

    print(transformList(list1, list2))


def main():
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    task1(str(namespace.file1, namespace.file2))

if __name__ == '__main__':
    main()
