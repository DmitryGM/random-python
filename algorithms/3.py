import helper


def number_ones(a):
    count = 0
    for xs in a:
        for x in xs:
            if x == 1:
                count += 1
    return count


def read_matrix():
    with open('v.txt', 'r') as file:
        n = int(file.readline())
        m = [[0]*n for _ in range(n)]
        for i in range(n):
            s = file.readline().split(' ')
            for j in range(n):
                if i < j:

                    if i - j == -1 or i == 0 and j == 11:
                        m[i][j] = 0
                    else:
                        m[i][j] = 0 if '-' in s[j] else 1
                else:
                    m[i][j] = 0
        helper.print_matrix(m)
        return n, m




_, a = read_matrix()

# #         1  2  3  4  5  6  7  8  9 10 11 12
# a.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]) # 1
# a.append([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]) # 2
# a.append([0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1]) # 3
# a.append([0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]) # 4
# a.append([0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0]) # 5
# a.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]) # 6
# a.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]) # 7
# a.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]) # 8
# a.append([0] * 12) # 9
# a.append([0] * 12) # 10
# a.append([0] * 12) # 11
# a.append([0] * 12) # 12

n = number_ones(a)
print(f'n = {n}')
matrix = [[0]*n for _ in range(n)]

edge_number = 0

d = dict()
for i in range(12):
    for j in range(12):
        if a[i][j] == 1:
            d[(i, j)] = edge_number
            edge_number += 1


for i in range(12):
    for j in range(12):
        if a[i][j] == 0:
            continue
        assert a[i][j] == 1
        assert i < j

        count = 0
        b = []

        for k in range(i+1, j):
            for m in range(j+1, i + 12):
                mm = m % 12
                kk = k
                if mm < kk:
                    # swap
                    (mm, kk) = (kk, mm)
                assert kk < mm
                assert a[mm][kk] == 0

                if a[kk][mm] == 1:
                   count += 1
                   b.append((kk+1, mm+1))

                   e1 = d[(kk, mm)]
                   e2 = d[(i, j)]

                   matrix[e1][e2] = 1
                   matrix[e2][e1] = 1

        print(f'i, j, count = {i+1, j+1, count}')
        print(b)


for i in range(n):
    matrix[i][i] = 1


print('Print matrix:')
for row in matrix:
    print(' '.join(map(str, row)))


if __name__ == '__main__':
    pass