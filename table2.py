from random import randint

m = int(input('количество строчек  '))
n = int(input('количество колонок  '))

matrix = [[randint(1, 50) for _ in range(m)] for _ in range(n)]


def show(lst):
    tmp = [0] * len(lst)
    for i in range(len(lst)):
        line_sum = 0
        for j in range(len(lst[i])):
            print('{:>4}'.format(lst[i][j]), end='')
            tmp[j] += lst[i][j]
            line_sum += lst[i][j]

        print('{:>10}'.format(line_sum))

    print()
    for i in range(len(tmp)):
        print('{:>4}'.format(tmp[i]), end='')
    print()


show(matrix)