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

    res = []
    for i in range(len(lst) // 3):
        res.append(f'{lst[3*i+1]} {i+1}')
        res.append(f'{lst[3*i+2]} {i+1}')

    return [filename[4:8]] + sorted(res)


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)

    for arg in args:
        extr_name(arg)


if __name__ == '__main__':
    print(extr_name('name2006.html')[:11])
    #main()
