#!/bin/python3

n = list(map(int, input().strip().split(' ')))
s = sum(n)

print('{} {}'.format(s - max(n), s - min(n)))
