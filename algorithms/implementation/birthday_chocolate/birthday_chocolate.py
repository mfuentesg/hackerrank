#!/bin/python3


n = int(input().strip())
s = [int(x) for x in input().strip().split(' ')]
d, m = (int(x) for x in input().strip().split(' '))
r = 0

for x in range(n-m+1):
    if sum(s[x:x+m]) == d:
        r += 1
print(r)
