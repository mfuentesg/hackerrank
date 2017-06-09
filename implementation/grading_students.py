#!/bin/python3

def get_grade(g):
  if g < 38 or g % 5 == 0:
    return g
  else:
    r = g % 10
    n = 5 if r < 5 else 10
    d = g - r + n
    return d if d - g < 3 else g

for _ in range(int(input().strip())):
   print(get_grade(int(input().strip())))
