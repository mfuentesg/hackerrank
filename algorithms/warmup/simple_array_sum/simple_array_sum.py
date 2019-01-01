#!/bin/python3

n = int(input().strip())
print(sum([int(x) for x in input().strip().split(' ')]))

# Simple version
# numbers = [int(x) for x in input().strip().split(' ')]
# t = 0
# for x in numbers:
#   t += x
# print(t)