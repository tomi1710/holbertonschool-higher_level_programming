#!/usr/bin/python3
"""
4. Text indentation
Write a function that prints a text with 2 new lines
after each of these characters: ., ? and :
Prototype: def text_indentation(text):"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    if text[0] == " ":
            while text[i] == " ":
                i = i + 1
    while i < len(text):
        if text[i] == "\n" and text[i + 1] == " ":
            print("")
            while text[i + 1] == " ":
                i = i + 1
            i = i + 1
        while (text[i] == "." or text[i] == "?" or text[i] == ":"):
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                if i == len(text) - 1:
                    break
                print("{}\n".format(text[i]))
                i = i + 1
                if text[i] == " ":
                    while text[i + 1] == " ":
                        i = i + 1
                    i = i + 1
                    continue
        print("{}".format(text[i]), end="")
        i = i + 1
