import random
import sys
import re


def mem_dict(filename):
    """
    :param filename:
    :return: dict: each word maps to list of words
    """
    file = open(filename, 'r')
    string = file.read()

    lst = re.findall(r'\w+', string)
    # print(lst)

    s = set()
    d = dict()
    d[''] = lst

    for i in range(len(lst)):
        if lst[i] in s:
            continue
        s.add(lst[i])
        d[lst[i]] = lst[i+1:]

    return d


def generate(d, n):
    """
    :param d: dict
    :param n: number words in the final text
    :return: string (final text)
    """
    res = ['']
    for i in range(n):
        last_word = res[i]
        res.append(d[last_word][random.randint(0, len(d[last_word]) - 1)])
    return ' '.join(res)


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)

    filename = sys.argv[1]
    print(generate(mem_dict(filename), 10))


if __name__ == '__main__':
    # print(generate(mem_dict('D:\\random-python\\file.txt'), 10))
    main()
