#!/bin/python3
import re

q = int(input().strip())

for i in range(q):
    s = input().strip().replace('1', '11')
    print(len(tuple(re.findall(r'1[0]{1,}1', s))))
