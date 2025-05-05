#!/usr/bin/python3

num = int(input("Enter a number\n"))

cnt = 0
while (cnt <= 9):
    result = num * cnt
    print(f"{cnt} x {num} = {result}")
    cnt += 1
