import math
import copy
import random
import numpy as np

from helper import print_matrix, checker, reader

random.seed(2019)


def print_perm(perm):
    res = list(range(len(perm)))
    for i, j in enumerate(perm):
        # swap i, j
        t = res[j]
        res[j] = res[i]
        res[i] = t
    print(f'res = {sorted(list(zip(res, range(len(perm)))))}')


def shuffle_matrix(m):
    n = len(m)
    m = np.array(m)
    perm = list(range(n))
    random.shuffle(perm)
    print_perm(perm)
    for i, j in enumerate(perm):
        # swap rows
        m[[i, j]] = m[[j, i]]

        # swap columns
        m[:, [i, j]] = m[:, [j, i]]

    return list(m.tolist())


def get_number_edges(m):
    n = len(m)
    count = 0
    for i in range(n):
        for j in range(i):
            if m[i][j] != -1 and m[i][j] != 0:
                count += 1
    return count


def count_components(m):
    def dfs(v):
        if colors[v]:
            return 0
        colors[v] = True
        for i in range(n):
            dfs(i)
        return 1

    n = len(m)
    colors = [False]*n
    res = 0
    for i in range(n):
        res += dfs(i)
    return res


def get_sequence(m):
    n = len(m)
    degs = [0]*n
    for i in range(n):
        for j in range(n):
            if m[i][j] != -1 and m[i][j] != 0:
                degs[i] += 1
    # [(deg, number)]
    return sorted(list(zip(degs, range(n))), key=lambda x: x[0])


def test_isomorphism(m1, m2):
    n1 = len(m1)
    n2 = len(m2)

    print('\n1.')
    print('Check number of vertices')
    print(f'{n1} == {n2}')

    print('\n2.')
    print('Check number of edges')
    e1 = get_number_edges(m1)
    e2 = get_number_edges(m2)
    print(f'{e1} == {e2}')

    print('\n3.')
    print('Check number of components')
    print(f'{count_components(m1)} == {count_components(m2)}')

    print('\n4.')
    print('Check deg sequence')
    print(get_sequence(m1))
    print(get_sequence(m2))

    # 5. Плотность f(G) – число вершин клики графа G.
    # Сложно.

    shuffle_matrix(m1)


def main():
    _, m1 = reader('input-17.txt')
    checker(m1)

    m2 = shuffle_matrix(m1)
    checker(m2)

    print_matrix(m1)
    print_matrix(m2)

    test_isomorphism(m1, m2)


if __name__ == '__main__':
    main()
