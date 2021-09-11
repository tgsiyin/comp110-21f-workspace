"""Repeating a beat in a loop."""

__author__ = "730272419"
# Begin your solution here...

count: int = 1
repeat_words: str = input("What beat do you want to repeat? ")
repeat_times: int = int(input("How many times you want to repeat? "))
after_required_numbers_of_repetition: str = repeat_words
if repeat_times <= 0:
    print("No beat...")
else: 
    while count < repeat_times:
        count = count + 1
        after_required_numbers_of_repetition = after_required_numbers_of_repetition + " " + repeat_words
print(after_required_numbers_of_repetition)