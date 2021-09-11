"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 

# Begin your solution here...
from random import randint
print("Your fortune cookie says...")
furtune_random_number: int = randint(1, 4)
SECRET_NUMBER_1: int = 1
SECRET_NUMBER_2: int = 3
if furtune_random_number == SECRET_NUMBER_1:
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if furtune_random_number == SECRET_NUMBER_2:
        print("Your life will be happy and peaceful.")
    else:
        if furtune_random_number < SECRET_NUMBER_2:
            print("Soon life will become more interesting.")
        else: 
            if furtune_random_number > SECRET_NUMBER_2:
                print("Soon you will become a super rich")
print("Now, go spread positive vibes!")