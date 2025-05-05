#!/usr/bin/python3

import sys

def downcase_it(txt : str) -> str:
    return txt.lower()

argv = sys.argv
if len(argv) > 1:
    for txt in argv:
        print(downcase_it(txt))
else:
    print("none")