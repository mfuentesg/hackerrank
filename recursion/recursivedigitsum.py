#!/bin/python3

def super_digit(s):
    if s < 10:
        return s
    return super_digit(split_sum(s))

def split_sum(n, k = None):
    return sum([int(x) * k if k else int(x) for x in str(n)])

n, k = input().strip().split(' ')
print(super_digit(split_sum(n, int(k))))
