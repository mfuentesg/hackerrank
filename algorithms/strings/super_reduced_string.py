#!/bin/python3

def solve(s):
    f = []
    for i in range(len(s) - 1):
        if i + 1 in f or i in f:
            continue

        if s[i] == s[i + 1]:
            f.append(i + 1)
            f.append(i)

    if len(f) == 0:
        return 'Empty String' if len(s) == 0 else s
    else:
        return solve(''.join(['' if i in f else s[i] for i in range(len(s))]))

print(solve(input().strip()))
