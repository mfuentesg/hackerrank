#!/bin/python3


def day_of_programmer(y):
    t = 215
    if y <= 1917:
        t = t + (29 if y % 4 == 0 else 28)
    elif y > 1918:
        t = t + (29 if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else 28)
    else:
        # february ---> 28 is not a leap year
        # 32th day of the year february 14th -> 28 - 14 + 1
        t = t + 15
    return '{}.09.{}'.format(256-t, y)


print(day_of_programmer(int(input().strip())))
