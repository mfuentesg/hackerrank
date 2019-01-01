#!/bin/python3

n = int(input().strip())
arr = input().strip().split(' ')
print(' '.join([arr[-1 * i] for i in range(1, n + 1)]))
