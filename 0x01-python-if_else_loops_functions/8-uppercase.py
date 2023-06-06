#!/usr/bin/python3
def uppercase(string):
    for c in string:
        value = ord(c)
        if value >= 97 and value <= 122:
            uppercase_char = chr(value - 32)
        else:
            uppercase_char = c
        print(uppercase_char, end="")
    print()