import sys
from lxml import html


def extr_name(filename):
    """
    :param filename: nameYYYY.html
    :return: list started with year, continue name-rank (asc) '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', '
    """

    file = open(filename, 'r')
    string = file.read()

    tree = html.fromstring(string)


    lst = tree.xpath('//table[1]/tr/td/text()')
    males = []
    females = []

    for i in range(30):
        if i % 3 == 1:
            males.append(lst[i])
        if i % 3 == 2:
            females.append(lst[i])

    print(males)
    print(females)

    return


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)

    for arg in args:
        extr_name(arg)


if __name__ == '__main__':
    extr_name('name2006.html')
    #main()
