# Program for removing punctuation from text
# Author: @aadnanmt
# Date: 2023-10-01
# Description: This program removes punctuation from the input text.

import string

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

print("")
print("// code by @aadnanmt //")
print("")
text = input("Enter the text here, okay?: ")

print(f"This is your original text: {text}")
print(f"Text without punctuation:", remove_punctuation(text))