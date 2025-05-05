#!/usr/bin/python3

import sys, re

if len(sys.argv) == 3:
    n = len(re.findall(sys.argv[1], sys.argv[2]))
    print(n)
else:
    print("none")
