"""This is a game of you going on an adventure to the Magic Black Forest."""
__author__ = "730272419"
import random
points: int
player: str


def main() -> None:
    """This is the game's entry point; where your adventure starts!"""
    greet()
    global points
    points = 0
    NAMED_CONSTANT: str = '\U0001F332'
    exit_game: int = 1
    choice: int = int(input("Enter '1' if you want to leave the realm of the Magic Black Forest. Enter '2' if your goal is the herb field. Enter '3' if you are seeking forest monsters: "))
    while choice != exit_game:
        if choice == 2:
            herbfield()
        if choice == 3:
            hunt_monster(points)
            print(f"{player}, current points: {points}")
        choice = int(input("Continue to play, enter a number to select next route: "))
    print(f"{NAMED_CONSTANT}You exit the adventrue, and here is your experience points: {points}")


def greet() -> None:
    """This is greeting message."""
    print("You entered the realm of Magic Black Forest. You will have three options presented to you each time you complete a search in the forest. The forest is dangerous, so be mindful with your choices.")
    global player
    player = input("Enter your name: ")
    

def hunt_monster(x: int) -> int:
    """This is function of player who choose hunting branch of Black Forest search."""
    power: int = 10
    exit_monster_blood: int = 30
    player_choice: int = int(input((f"Warning! {player}, you have entered the territory of monsters. Before you proceed, be sure that your current points is above the power standard, or you will be killed by a monster and lose all your points. Once you started, you can only leave until you obtain 30 monster blood. A successful hunt journey will earn you 10 points. Enter '1' to go on hunting and enter '2' to leave: ")))
    if player_choice == 1:
        blood_collected: int = 0
        if x < power:
            x = - x
            return x
        else:
            while blood_collected < exit_monster_blood:
                hunt: int = int(input("Make a hunt number between 1 and 100: "))
                if hunt < 30:
                    blood_collected = blood_collected + 5
                elif hunt < 40:
                    blood_collected = blood_collected + 10
                elif hunt < 70:
                    blood_collected = blood_collected + 15
                else:
                    blood_collected = blood_collected + 1
            return 10
    else:
        return 0
        

def herbfield() -> None:
    """This is function of player who choose herb searching branch of Black Forest adventure."""
    global points
    global player
    player_action: str = input(player + ", " "Start search? Enter 'Yes' for a search, 'No' to leave herbfiled: ")
    if player_action == "Yes":
        herb_found: int = random.randint(1, 10)
        search: bool = bool(herb_found % 2 == 0)
        if search:
            points = points + 5
            print(f"{player}, current points: {points}")
        else:
            points = points + 1
            print(f"{player}, current points: {points}")
    else:
        print(f"{player}, current points: {points}")


if __name__ == "__main__":
    main()