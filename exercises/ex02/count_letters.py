"""Counting letters in a string."""

__author__ = "730272419"
# Begin your solution here...
input_letter: str = input("What letter do you want to seach for?: ")
input_word: str = input("Enter a word: ")
length: int = len(input_word) - 1
count_1: int = 0
count_target: int = 0
while length >= count_1:
    character: str = input_word[count_1]
    if character == input_letter:
        count_target = count_target + 1
        count_1 = count_1 + 1
    else:
        count_target = count_target
        count_1 = count_1 + 1
print("Count: " + str(count_target))