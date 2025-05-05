#!/usr/bin/python3

import sys

argv = sys.argv 
n = len(argv)
if n == 3:
    output = list(range(int(argv[1]), int(argv[2]) + 1))
    print(output)
else:
    print("none")
