#!/bin/python3

alice = list(map(int, input().strip().split(' ')))
bob = list(map(int, input().strip().split(' ')))
a = 0
b = 0

for i, _ in enumerate(alice):
    if alice[i] > bob[i]:
        a += 1
    elif alice[i] < bob[i]:
        b += 1
        
print('{} {}'.format(a, b))
