"""Drawing forests in a loop."""

__author__ = "730272419"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
number_of_trees: int = int(input("Depth: "))
forests_growth: str = TREE
forests_growth1: str = ""
while number_of_trees > 0:
    print(forests_growth + forests_growth1)
    number_of_trees = number_of_trees - 1
    forests_growth1 = forests_growth1 + TREE