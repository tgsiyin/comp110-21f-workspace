"""Finding duplicate letters in a word."""

__author__ = "730272419"

input_word: str = input("Enter a word: ")
length_inputword: int = len(input_word)
c_ommand: int = 0
char_count: int = length_inputword - 1
char_begin: int = 0
char_count1: int = 1
while char_begin < length_inputword:
    while char_count1 < length_inputword:
        if str(input_word[char_begin]) == str(input_word[char_count1]):
            c_ommand = c_ommand + 1 
        char_count1 = char_count1 + 1
    char_begin = char_begin + 1
    char_count1 = char_begin + 1
if c_ommand > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")
