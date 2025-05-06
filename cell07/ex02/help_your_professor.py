#!/usr/bin/python3

def average(input_dict : dict) -> float:
    sum = 0
    cnt = 0
    for k, v in input_dict.items():
        sum += v
        cnt += 1
    return sum / cnt

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")