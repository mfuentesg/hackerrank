#!/bin/python3

A = []

for _ in range(6):
    A.append([int(i) for i in input().strip().split(' ')])

def solve(A):
    hgs=[]
    sums=[]

    for i in range(4):
        for j in range(4):
            hgs.append(hourglasses(A, 3, i, j))

    for i in range(len(hgs)):
        for j in range(len(hgs)):
            if j == 3 or j == 5:
                hgs[i][j]=0

    for hg in hgs:
        sums.append(sum(hg))

    return max(sums)

def hourglasses(A, dimension, i, j):
    hg=[]
    for hgi in range(i, i + dimension):
        for hgj in range(j, j + dimension):
            hg.append(A[hgi][hgj])
    return hg

print(solve(A))
