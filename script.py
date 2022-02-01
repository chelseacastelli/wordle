
from rich.console import Console
import random

console = Console()

words = [
    "jazzy",
    "jumps",
    "enzym",
    "fuzzy",
    "chute",
    "sheer",
    "cozey",
    "field"
]

def split(word):
    return [char for char in word]


def random_word(words):
    return random.choice(words)


def check_guess(word, guess):
    output = ''

    if guess == word:
        return 1

    for index, char in enumerate(guess):
        if char in word:
            if char == word[index]:
                output += f'[bold green][u]{char}[/u][/bold green] '
            else:
                output += f'[bold yellow][u]{char}[/u][/bold yellow] '
        else:
            output += f'[u]{char}[/u] '


    console.print(output)
    return 0


word = random_word(words)
word_list = split(word)
guesses = []
chances = 1

while chances <= 5:
    valid_word = False

    while not valid_word:
        user_guess = split(input('\nGuess word: '))

        if len(user_guess) > 5 or len(user_guess) < 5:
            print('Your guess must be 5 characters long.\n')

        elif user_guess in guesses:
            print('You already guessed that word.\n')

        else:
            valid_word = True

    guesses.append(user_guess)

    if check_guess(word_list, user_guess):
        console.print('\n[bold cyan]YOU WIN![/bold cyan]')
        break

    chances += 1

    if chances > 5:
        console.print('\n[bold red]You lose![/bold red]')
        console.print(f'The word was [i]{word}[/i]')

