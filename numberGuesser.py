from random import randint
from rich.console import Console
import argparse

console = Console()
parser = argparse.ArgumentParser(prog="game", description="Number Gesser Game")
subparsers = parser.add_subparsers(dest="command")
starting_message = """
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
"""
random_number = randint(1, 1000)

parser_start = subparsers.add_parser("start", help="Start the game")
args = parser.parse_args()


def game_logic(difficult: str) -> None:
    count = 0
    match difficult:
        case "1":
            console.print(
                "Great! You have selected the Easy difficulty level. You have 10 chances. Let's start the game!",
                style="bold purple",
            )
            while count < 10:
                user_guess = int(input("Enter your guess: "))
                if user_guess == random_number:
                    console.print(
                        f"Congratulations! You guessed the correct number in {count+1} attempts.",
                        style=("bold green"),
                    )
                    break
                elif user_guess < random_number:
                    console.print(
                        f"Incorrect! The number is greater than {user_guess}.",
                        style="bold red",
                    )
                    count += 1
                else:
                    console.print(
                        f"Incorrect! The number is less than {user_guess}.",
                        style=("bold red"),
                    )
                    count += 1
        case "2":
            console.print(
                "Great! You have selected the Medium difficulty level. You have 5 chances. Let's start the game!",
                style="bold purple",
            )
            while count < 5:
                user_guess = int(input("Enter your guess: "))
                if user_guess == random_number:
                    console.print(
                        f"Congratulations! You guessed the correct number in {count+1} attempts.",
                        style="bold green",
                    )
                    break
                elif user_guess < random_number:
                    console.print(
                        f"Incorrect! The number is greater than {user_guess}.",
                        style="bold red",
                    )
                    count += 1
                else:
                    console.print(
                        f"Incorrect! The number is less than {user_guess}.",
                        style="bold red",
                    )
                    count += 1
        case "3":
            console.print(
                "Great! You have selected the Hard difficulty level. You have 3 chances. Let's start the game!",
                style="bold purple",
            )
            while count < 3:
                user_guess = int(input("Enter your guess: "))
                if user_guess == random_number:
                    console.print(
                        f"Congratulations! You guessed the correct number in {count+1} attempts.",
                        style="bold green",
                    )
                    break
                elif user_guess < random_number:
                    console.print(
                        f"Incorrect! The number is greater than {user_guess}.",
                        style="bold red",
                    )
                    count += 1
                else:
                    console.print(
                        f"Incorrect! The number is less than {user_guess}.",
                        style="bold red",
                    )
                    count += 1


if args.command == "start":
    print(starting_message)
    difficult = input("Enter your choice: ")
    game_logic(difficult)
