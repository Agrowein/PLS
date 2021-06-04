import sys

from utils import createParser, readFile, write_file, CharIterator


def task(data):
    return word_generator(CharIterator(data))


def find_words(func):
    def wrapper(itr):
        out = []
        for word in func(itr):
            for i in word:
                if word.count(i) >= 3:
                    out.append(word)
                    break
        return out
    return wrapper


@find_words
def word_generator(itr):
    word = ''
    for char in itr:
        if char.lower() in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчщшъыьэюя1234567890':
            word += char
        else:
            yield word
            word = ''
    yield word


def main():
    parameters = [
        ['--input', '-i'],
        ['--output', '-o']
    ]
    namespace = createParser(parameters).parse_args(sys.argv[1:])
    data = readFile(str(namespace.input), lambda f: f.read())
    result = task(data)
    write_file(result, str(namespace.output), lambda f, d: f.write(str(d)))


if __name__ == '__main__':
    main()
