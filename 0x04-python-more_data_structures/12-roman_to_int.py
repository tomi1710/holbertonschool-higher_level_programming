#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = 0
    a = 0
    if (roman_string is None):
        return (0)
    if isinstance(roman_string, str) is False:
        return (0)

    for i in range(len(roman_string) - 1):
        if roman_string[i] == 'M':
            roman = roman + 1000
        elif roman_string[i] == 'D':
            roman = roman + 500
        elif roman_string[i] == 'C':
            roman = roman + 100
        elif roman_string[i] == 'L':
            roman = roman + 50
        elif roman_string[i] == 'X':
            roman = roman + 10
        elif roman_string[i] == 'V':
            roman = roman + 5
        elif roman_string[i] == 'I':
            a = a + 1
    if (roman_string[-1] == 'I'):
        roman = roman + a + 1
    elif (roman_string[-1] == 'X'):
        roman = (roman + 10) - a
    elif (roman_string[-1] == 'V'):
        roman = (roman + 5) - a
    elif (roman_string[-1] == 'L'):
        roman = (roman + 50) - a

    return (roman)
