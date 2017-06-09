#!/bin/python3

_ = int(input().strip())
h = list(map(int, input().strip().split(' ')))
print(h.count(max(h)))
