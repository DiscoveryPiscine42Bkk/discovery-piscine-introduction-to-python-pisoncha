#!/usr/bin/python3

import sys

argv = sys.argv 
n = len(argv)
if n == 3:
    n_min = min(int(argv[1]), int(argv[2]))
    n_max = max(int(argv[1]), int(argv[2]))
    output = list(range(n_min, n_max + 1))
    print(output)
else:
    print("none")
