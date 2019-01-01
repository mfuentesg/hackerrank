#!/bin/python3

_, k = (int(x) for x in input().strip().split(' '))
bill = [int(x) for x in input().strip().split(' ')]
b = int(input().strip())

# correct answer
r = (sum(bill) - bill[k])//2
print('Bon Appetit' if r == b else b - r)
