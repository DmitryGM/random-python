import math
import copy
from helper import print_matrix, checker, reader


def get_neighbors(i):
    global n, m
    res = []
    for j in range(n):
        if m[i][j] != 0 and m[i][j] != -1:
            res.append(j)
    return res


# 1. Алгоритм, использующий упорядочивание вершин
def foo():
    global m, n

    colors = [-1]*n
    k = 1
    need_continue = True
    while need_continue:
        r = [0] * n
        for i in range(n):
            if colors[i] != -1:
                continue
            for j in range(n):
                r[i] += 1 if m[i][j] != -1 and m[i][j] != 0 and colors[j] == -1 else 0

        lst = list(zip(range(n), r))
        lst2 = list(reversed(sorted(lst, key=lambda p: p[1])))

        print(lst2)

        for i, _ in lst2:
            if colors[i] != -1:
                continue
            can_color = True
            for j in get_neighbors(i):
                if colors[j] == k:
                    can_color = False
            if can_color:
                colors[i] = k

        need_continue = False
        for c in colors:
            if c == -1:
                need_continue = True
        k += 1
        print(colors)
        print()

    return colors


# 2. Размещение элементов методом обратного размещения
def positions(m, n):
    p = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]

    def get_pair(x):
        x -= 1
        return ((x % 4), int(x / 4))

    dp = [[0]*12 for _ in range(12)]

    for i in range(12):
        for j in range(12):
            x1, y1 = get_pair(i+1)
            x2, y2 = get_pair(j+1)
            dp[i][j] = abs(x1 - x2) + abs(y1 - y2)

    print_matrix(dp)

    # Ri
    r = [0]*n
    for i in range(n):
        for j in get_neighbors(i):
            r[i] += m[i][j]
    r = sorted(list(zip(r, range(1, n+1))))

    # Di
    d = [0]*n
    for i in range(n):
        for j in range(n):
            d[i] += dp[i][j]
    d = sorted(list(zip(d, range(1, n+1))), key=lambda p: -p[0])

    print(r)
    print(d)


# 3. Дейкстра
def dijkstra():
    global m, n

    mm = copy.deepcopy(m)

    for i in range(n):
        for j in range(n):
            mm[i][j] = math.inf if m[i][j] == -1 else m[i][j]

    d = [[math.inf]*n for _ in range(n)]

    s = set()

    # start v:
    v = 0
    s.add(v)

    for i in range(n):
        d[0][i] = mm[0][i]

    min_i = -1

    for i in range(n):
        if i in s:
            continue
        if d[0][i] < d[0][min_i]:
            min_i = i

    s.add(min_i)
    print(d[0])
    print(min_i)

    for i in range(1, n):
        for j in range(n):
            d[i][j] = min(d[i-1][j], d[i-1][min_i] + mm[min_i][j])

        # select min_i:
        min_i = -1
        for j in range(n):
            if j in s:
                continue
            if min_i == -1:
                min_i = j
            if d[i][j] < d[i][min_i]:
                min_i = j

        s.add(min_i)
        print(d[i])
        print(min_i)


# 4. Поиск пропускной способности алгоритмом Франка-Фриша
def frank_fish(n, m):
    merged = [i for i in range(n)]

    # Исходный граф:
    step = 0
    print(f'step = {step}')
    print('Source graph:')
    print_matrix(m)

    for step in range(1, 6):
        print(f'step = {step}')

        # cut:
        max_w = -1
        for i in range(n):
            if merged[i] != i:
                continue

            max_w = max(max_w, m[i][0])

        print(f'max_w = {max_w}')

        # merge:
        for i in range(n):
            for j in range(i):
                if m[i][j] >= max_w:
                    merged[i] = j

        # update merged
        need_next = True
        while need_next:
            need_next = False
            for i in range(len(merged)):
                if merged[i] != i and merged[i] != merged[merged[i]]:
                    merged[i] = merged[merged[i]]
                    need_next = True

        print('merged:')
        print(merged)

        lst = [set() for _ in range(n)]
        for i in range(n):
            if i != merged[i]:
                lst[merged[i]].add(i)

        # update matrix:
        for i in range(n):
            if lst[i]:
                for j in lst[i]:
                    for k in range(n):
                        if k != i:
                            m[k][i] = max(m[k][i], m[k][j])
                            m[i][k] = m[k][i]
        print(lst)

        new_m = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if merged[i] == i and merged[j] == j:
                    new_m[i][j] = m[i][j]

        m = new_m
        checker()
        print_matrix(m)






if __name__ == '__main__':
    pass


reader('input-17.txt')
checker()

print_matrix(m)

# foo()

# positions(m, n)

# dijkstra()
frank_fish(n, m)
