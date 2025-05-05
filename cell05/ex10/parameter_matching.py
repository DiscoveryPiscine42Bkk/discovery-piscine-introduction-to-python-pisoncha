#!/usr/bin/python3

import sys

if len(sys.argv) == 2:
    input_param = input("What was the parameter? ")
    if (input_param == sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
