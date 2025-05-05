#!/usr/bin/python3

def greetings(str_input : str = "noble stranger") -> None:
    if type(str_input) == str:
        print(f"Hello, {str_input}.")
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)