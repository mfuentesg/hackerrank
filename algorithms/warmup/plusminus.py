#!/bin/python3

n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
nbs = { 'p': 0, 'n': 0, 'z': 0 }

for n in arr:
    if n > 0:
        nbs['p'] += 1
    elif n < 0:
        nbs['n'] += 1
    else:
        nbs['z'] += 1

print('{0:.6f}'.format(nbs['p'] / len(arr)))
print('{0:.6f}'.format(nbs['n'] / len(arr)))
print('{0:.6f}'.format(nbs['z'] / len(arr)))
