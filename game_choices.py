"""I want to see if I can write a program where you can choose which game will run.
Users answer the prompt, 'Which game do you want to play? (game1/game2/game3) ' and
that game will launch for them. Games are imported modules, so you can add more options
over time.
"""

import roshambo
import turtle_test
from enum import IntEnum

class Action(IntEnum):
    roshambo = 0
    turtle_test = 1

user_name = input("Welcome to Game Choices! Let's get started.\nWhat's your name?")

def get_user_choice():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    choices_str = ', '.join(choices)
    user_choice = int(input(f'{user_name}, enter a choice ({choices_str}): '))
    action = Action(user_choice)
    return action

#This while loop should execute the program and allow the game choice:
while True:
    try:
        user_action = get_user_choice()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid choice. Enter a value in range {range_str}.\n")
        continue