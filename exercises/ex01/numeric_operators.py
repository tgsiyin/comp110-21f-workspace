"""Ex01. Math operation of two input numbers."""
__author__ = "730272419"
left_hand_side: str = input("Enter left-hand side number: ")
right_hand_side: str = input("Enter right-hand side number: ")
print("Left-hand side: " + left_hand_side)
print("Right-hand side: " + right_hand_side)
left_hand_side_integer = int(left_hand_side)
right_hand_side_integer = int(right_hand_side)
left_hand_side_integer_to_the_power_of_right_hand_side_integer = int(left_hand_side_integer ** right_hand_side_integer)
left_hand_side_integer_divided_by_right_hand_side_integer = float(left_hand_side_integer / right_hand_side_integer)
whole_number_division_of_left_hand_side_integer_by_right_hand_side_integer = int(left_hand_side_integer // right_hand_side_integer)
reminder_of_left_hand_side_integer_devided_by_right_hand_side_integer = int(left_hand_side_integer % right_hand_side_integer)
print(left_hand_side + " ** " + right_hand_side + " is " + str(left_hand_side_integer_to_the_power_of_right_hand_side_integer))
print(left_hand_side + " / " + right_hand_side + " is " + str(left_hand_side_integer_divided_by_right_hand_side_integer))
print(left_hand_side + " // " + right_hand_side + " is " + str(whole_number_division_of_left_hand_side_integer_by_right_hand_side_integer))
print(left_hand_side + " % " + right_hand_side + " is " + str(reminder_of_left_hand_side_integer_devided_by_right_hand_side_integer))