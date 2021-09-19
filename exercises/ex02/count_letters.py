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

a: int = 8
b: int = 2
c: int = 0
i: int = 2

while a > b:
    if a % 2 == 0:
        b = b + 2 
    elif a % 3 == 0:
        b = b + 1
    elif a % 2 == 1:
        if a % 7 == 0:
            while i > 0:
                b = b - i
                i = i - 1
            i = 2
        b = b + 1
    a = a - 1
    c = c + 1 

print(a)
print(b)
print(c)

x: float = 3
y: float = 5
x = x - 1 

if x < y: 
    z = x ** y / 2
else: 
    if x == y:
        z = y % x
    else: 
        x = x / 2
        z = y - x
    z = z + 1
print(z)