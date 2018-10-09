from itertools import groupby


def rm_adj(nums):
    """
    :param nums:
    :return:
    """
    # [(el, list(ee)) for el, ee in groupby(nums)]
    return [el for el, _ in groupby(nums)]


def union(a, b):
    """
    :params a, b: lists
    :return: sorted(a + b)
    """
    return sorted(a + b)


def main():
    print(union([1, 2, 3], [0, 11, 12]))
    print(rm_adj([0, 3, 0, 1, 2, 2, 3, 3, 3]))


if __name__ == '__main__':
    main()
