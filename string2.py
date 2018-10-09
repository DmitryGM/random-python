

def v(s):
    """
    :param s: string
    :return: If length > 3, add to the end "ing", if in the end not already "ing", else add "ly".
    """
    if len(s) > 3 and s[-3:] != 'ing':
        return s + 'ing'
    else:
        return s + 'ly'


def nb(s):
    """
    So 'This music is not so bad!' -> This music is good!
    :param s: string
    :return: Replase substring from 'not' to 'bad'. ('bad' after 'not') to 'good'.
    """
    # print(s.find('not'))
    # print(s.find('bad'))
    return s[:s.find('not')] + 'good' + s[s.find('bad') + 3:]


def main():
    print(nb('This music is not so bad!'))


if __name__ == '__main__':
    main()
