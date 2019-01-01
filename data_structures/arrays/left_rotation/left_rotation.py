#!/bin/python3

n, d = list(map(int, input().strip().split(' ')))
A = input().strip().split(' ')

if d != len(A):
    A = A[d:] + A[:d]

print(' '.join(A))
