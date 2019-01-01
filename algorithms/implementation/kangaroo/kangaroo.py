#!/bin/python3

x1, v1, x2, v2 = list(map(int, input().strip().split(' ')))
m = abs(x1 - x2) // abs(v1 - v2) if abs(v1 - v2) > 0 else 1

p1d = x1 + v1 * m
p2d = x2 + v2 * m

print('YES' if p1d == p2d else 'NO')
