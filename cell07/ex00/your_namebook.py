#!/usr/bin/python3

def array_of_names(input_dict : dict) -> list:
    output = []
    for k,v in input_dict.items():
        output.append(k.capitalize() + " " + v.capitalize())
    return output

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))