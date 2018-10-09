import sys
#from lxml import html


def extr_name(filename):
    """
    :param filename: nameYYYY.html
    :return: list started with year, continue name-rank (asc) '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', '
    """

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
