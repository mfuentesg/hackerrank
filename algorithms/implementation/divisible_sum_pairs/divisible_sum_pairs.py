#!/bin/python3

n, k = list(map(int, input().strip().split(' ')))
a = list(map(int, input().strip().split(' ')))

s = 0
for i in range(n):
  for j in range(i + 1, n):
    s += 1 if (a[i] + a[j]) % k == 0 and i < j else 0

print(s)
