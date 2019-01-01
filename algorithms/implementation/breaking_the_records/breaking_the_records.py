#!/bin/python3


def solve(n, s):
    l = 0
    h = 0
    li = s[0]
    hi = s[0]

    for i in s:
        if i < li:
            l += 1
            li = i
        if i > hi:
            h += 1
            hi = i
    return h, l


n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
h, l = solve(n, s)
print('{} {}'.format(h, l))
