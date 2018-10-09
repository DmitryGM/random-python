

def me(words):
    """
    :param words: list of strings
    :return: count strings where len(string) > 2 and first char == last char
    """
    count = 0
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count += 1
    return count


def fx(words):
    """
    ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc'] -> ['aabbbccc', 'apple', 'tix']
    :param words: list of strings
    :return: sorted list of strings with the exception of all strings started with 'x'
    """
    res = []
    for word in sorted(words):
        if word[0] != 'x':
            res.append(word)
    return res


def sort_tuples(list_tuples):
    """
    [(1, 7), (1, 3), (3, 4, 5), (2, 2)] -> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    :param list_tuples: list of non-empty tuples
    :return: sorted list by ascending the last element of tuple
    """
    return sorted(list_tuples, key=lambda x: x[-1])


def main():
    print(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']))


if __name__ == '__main__':
    main()
