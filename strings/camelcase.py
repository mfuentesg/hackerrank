#!/bin/python3
import re

print(len(re.sub('[a-z]', '', input().strip())) + 1)
