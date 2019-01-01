#!/bin/python3


def convert(t, f):
    h, m, s = list(map(int, t.split(':')))

    def to_str(h):
        if h < 10:
            return '0{}'.format(h)
        return h

    if f == 'PM' and h < 12:
        h += 12

    if f == 'AM' and h == 12:
        h = 0

    return '{}:{}:{}'.format(to_str(h), to_str(m), to_str(s))


i = input().strip()
t = i[0:-2]
f = i[-2:]

print(convert(t, f))
