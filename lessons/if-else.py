"""Challenge Question 1"""

# Print A if choice < 25
# Print B if choice < 50
# Print C if choice > 75
# Print D if choice >=50 and <= 75

choice: int = int(input("put a number of your choice: "))
if choice < 25: 
    print("A")
else: 
    if choice < 50:
        print("B")
    else:
        if choice <= 75:
            print("C")
        else:
            print("D")

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
            b = b - i
            i = i - 1
        i = 2
        b = b + 1
    a = a - 1
    c = c + 1 

    print(a + b + c)
