import torch
def main():
    # Open the input file
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    # Get each character from the text
    chars = sorted(list(set(text)))

    # Map each character to integer that is in the text
    stringToInt = {}
    intToString = {}

    # Create the string to integer encoding
    for i, char in enumerate(chars):
        stringToInt[char] = i

    # Create the integer to string encoding
    for i, char in enumerate(chars):
        stringToInt[i] = char

    # encoder function
    encode = lambda string: [stringToInt[char] for char in string]

    # decoder function
    decode = lambda intlist: [intToString[i] for i in intlist]

    # encode all text and wrap it into a tensor
