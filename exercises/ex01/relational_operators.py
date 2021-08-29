"""Ex01. Boolean function carried out comparing two input numbers"""
__author__ = "730272419"
left_hand_side: str = input("Enter left-hand side number: ")
right_hand_side: str = input("Enter right-hand side number: ")
print("Left-hand side: " + left_hand_side)
print("Right-hand side: " + right_hand_side)
the_boolean_value_of_whether_left_hand_side_integer_is_smaller_than_right_hand_side_integer = bool(int(left_hand_side) < int(right_hand_side))
the_boolean_value_of_whether_left_hand_side_integer_is_larger_than_or_equal_to_right_hand_side_integer = bool(int(left_hand_side) >= int(right_hand_side))
the_boolean_value_of_whether_left_hand_side_integer_is_equal_to_right_hand_side_integer = bool(int(left_hand_side) == int(right_hand_side))
the_boolean_value_of_whether_left_hand_side_integer_is_not_equal_to_right_hand_side_integer = bool(int(left_hand_side) != int(right_hand_side))
print(left_hand_side + " < " + right_hand_side + " is " + str(the_boolean_value_of_whether_left_hand_side_integer_is_smaller_than_right_hand_side_integer))
print(left_hand_side + " >= " + right_hand_side + " is " + str(the_boolean_value_of_whether_left_hand_side_integer_is_larger_than_or_equal_to_right_hand_side_integer))
print(left_hand_side + " == " + right_hand_side + " is " + str(the_boolean_value_of_whether_left_hand_side_integer_is_equal_to_right_hand_side_integer))
print(left_hand_side + " != " + right_hand_side + " is " + str(the_boolean_value_of_whether_left_hand_side_integer_is_not_equal_to_right_hand_side_integer))