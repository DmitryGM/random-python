import math
import copy


def reader(filename: str):
    with open(filename, 'r') as file:
        n = int(file.readline())
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            s = file.readline().split(' ')
            for j in range(n):
                m[i][j] = -1 if '-' in s[j] else int(s[j])
        return n, m


def checker(m):
    n = len(m)
    for i in range(n):
        for j in range(i, n):
            assert m[i][j] == m[j][i]
            # if m[i][j] != m[j][i]:
            #     print(f'(i,j) != ({i},{j})')


def print_matrix(m):
    n = len(m)
    print(' '*3 + ' '.join(list(map(lambda x: f' {x}' if x < 10 else str(x), range(n)))))

    for i in range(n):
        print((f'{i} ' if i < 10 else str(i)) + ' ' + ' '.join(list(map(lambda x: f' {x}' if x >= 0 else f'--', m[i]))))
    print()