"""
Project 1: Pig game
"""

from time import sleep
from random import randint


def roll_dice() -> int:
    """
    Simulate the roll of a dice.

    Returns:
        int: An integer value between 1 and 6.
    """

    print("Rolling the dice...", end=" ")
    sleep(1)

    dice = randint(1, 6)

    print(f"The dice landed on {dice}!")
    return dice


def turn(turn_rolls: int) -> int:
    """
    Simulate a turn of the game.

    Args:
        turn_rolls (int): The number of dice rolls in the turn.

    Returns:
        int: The score for the turn. If a 1 is rolled, the score for the turn is 0.
    """

    turn_score = 0

    for _ in range(turn_rolls):
        dice = roll_dice()
        if dice != 1:
            turn_score += dice
        else:
            turn_score = 0
            break

    print(f"\nThe turn score is {turn_score}!\n")
    return turn_score


player_score = 0
computer_score = 0

WINNING_SCORE = 50

invalid_input = False

print(
"""
--- PIG GAME ---

At each turn, you have to choose how many times you'll roll the dice
The number the dice lands on, it is added to your score
If the dice lands at 1, you lose the turn score
Whoever gets 50 points of score, wins the game!
""")

while player_score < WINNING_SCORE and computer_score < WINNING_SCORE:
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}\n")

    # Check if the player entered an valid input
    try:
        player_turn_rolls = input("It's your turn! How many times you wish to roll the dice? \n- ")

        player_turn_rolls = int(player_turn_rolls)
    except ValueError:
        invalid_input = True
        player_score = 0

        break

    # The computer chooses a random number of rolls
    computer_turn_rolls = randint(2, 10)

    player_score += turn(player_turn_rolls)
    computer_score += turn(computer_turn_rolls)

# Determine the winner
if player_score > computer_score:
    print(f"Congratulations! You won with {player_score} points!")
elif computer_score > player_score:
    print(f"The computer won! with {computer_score} points! Better luck next time!")
elif invalid_input:
    print("You entered an invalid input. Please try again.")
else:
    print(f"It's a tie! You both have the same score ({player_score})!")
