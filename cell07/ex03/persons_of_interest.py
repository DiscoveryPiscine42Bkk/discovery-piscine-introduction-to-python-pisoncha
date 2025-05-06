#!/usr/bin/python3

def famous_births(input_dict : dict) -> None:
    # convert a nested dict to a normal dict
    temp = {}
    for k, v in input_dict.items():
        temp[v["name"]] = v["date_of_birth"]
    
    # sort by value
    temp = dict(sorted(temp.items(), key=lambda item: item[1]))

    # print results
    for k, v in temp.items(): 
        print(f"{k} is a great scientist born in {v}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

famous_births(women_scientists)