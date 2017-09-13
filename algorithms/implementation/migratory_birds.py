#!/bin/python3

def solve(b):
    d = {}
    l = []
    m = 0

    for x in b:
        d[x] = d[x] + 1 if x in d else 1
        m = d[x] if d[x] > m else m

    for v, x in d.items():
        if x == m:
            l.append(v)

    return min(l)

_ = int(input().strip())
print(solve(list(map(int, input().strip().split(' ')))))
