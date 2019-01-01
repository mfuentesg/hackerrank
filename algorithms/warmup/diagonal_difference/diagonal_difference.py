#!/bin/python3

n = int(input().strip())
a = [list(map(int, input().strip().split(' '))) for x in range(n)]

ld = 0
rd = 0
for i, e in enumerate(a):
    for j, f in enumerate(a):
        if j + i == len(a) - 1:
            rd += a[i][j]

        if j == i:
            ld += a[i][j]

print('{}'.format(abs(ld - rd)))
