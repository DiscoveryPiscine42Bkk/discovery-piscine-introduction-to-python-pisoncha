#!/usr/bin/python3

def add_one(n : int) -> int:
    n += 1
    return n

n = 42
print(f"Before : {n}")
n = add_one(n)
print(f"After  : {n}")