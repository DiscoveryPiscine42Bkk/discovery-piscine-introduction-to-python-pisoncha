#!/usr/bin/python3

def find_the_redheads(input_dict : dict) -> list:
    return list(filter(lambda x : input_dict[x] == "red", input_dict))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))