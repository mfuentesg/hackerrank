#!/bin/python3

import re

s = input().strip().replace(' ', '').lower()

while re.search(r'([a-z])(.*)\1', s):
    s = re.sub(r'([a-z])(.*)\1', r'\1\2', s)

print('pangram' if len(s) == 26 else 'not pangram')
