#!/usr/bin/python3

import sys

if len(sys.argv) == 1:
    for i in range(11):
        output_str = f"Table de {i}:"
        for j in range(11):
            res = i * j
            output_str += f" {res}"
        print(output_str)
else:
    print("none")