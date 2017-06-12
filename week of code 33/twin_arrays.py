#!/bin/python3

n = int(input().strip())
A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))

As = sorted([(i, x) for i, x in enumerate(A)], key=lambda x: x[1])
Bs = sorted([(i, x) for i, x in enumerate(B)], key=lambda x: x[1])

if As[0][0] == Bs[0][0]:
    print(min(As[0][1] + Bs[1][1], As[1][1] + Bs[0][1]))
else:
    print(As[0][1] + Bs[0][1])
