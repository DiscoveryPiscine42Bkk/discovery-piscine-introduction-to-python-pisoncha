#!/usr/bin/python3

import sys

argv = sys.argv 
n = len(argv)
if n > 1:
    for i in range(1, n):
        if argv[i][-3:] != "ism":
            print(f"{argv[i]}ism")
else:
    print("none")
