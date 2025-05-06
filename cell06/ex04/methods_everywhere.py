#!/usr/bin/python3

import sys

def shrink(word : str) -> str:
    return word[:8]

def enlarge(word : str) -> str:
    i = len(word)
    while (i < 8):
        word = word + 'Z'
        i += 1
    return word

argv = sys.argv
if len(argv) > 1:
    for w in argv:
        if len(w) >= 8:
            print(shrink(w))
        else:
            print(enlarge(w))
else:
    print("none")