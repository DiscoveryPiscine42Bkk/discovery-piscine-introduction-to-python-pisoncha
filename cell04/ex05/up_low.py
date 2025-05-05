#!/usr/bin/python3
str_input = input()
output = ""
for c in str_input:
    if c.isupper():
        output += c.lower()
    elif c.islower():
        output += c.upper()
    else:
        output += c
print(output)
