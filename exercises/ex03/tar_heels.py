"""An exercise in remainders and boolean logic."""
__author__ = "730272419" 
# Begin your solution here...
input_number: int = int(input("Enter an int: "))

command_type1: bool = bool(input_number % 7 == 0 and input_number % 2 == 0)
command_type2: bool = bool(input_number % 2 == 0)
command_type3: bool = bool(input_number % 7 == 0)
if command_type1:
    print("TAR HEELS")
else:
    if command_type2:
        print("TAR")
    else:
        if command_type3:
            print("HEELS")
        else:
            print("CAROLINA")