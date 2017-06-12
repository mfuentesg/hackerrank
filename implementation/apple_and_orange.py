#!/bin/python3

s, t = list(map(int, input().strip().split(' ')))
a, b = list(map(int, input().strip().split(' ')))
m, n = list(map(int, input().strip().split(' ')))

print(len([1 for x in list(map(int, input().strip().split(' '))) if a + x in range(s, t + 1)]))
print(len([1 for x in list(map(int, input().strip().split(' '))) if b + x in range(s, t + 1)]))
