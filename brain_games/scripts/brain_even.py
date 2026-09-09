import random

import prompt

from brain_games.cli import print_wrong_answer, welcome_user


def is_even(number):
    return number % 2 == 0


def brain_even(name: str) -> None:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_tries = 3
    while count_tries > 0:
        random_int = random.randint(1, 1000)
        print(f'Question: {int(random_int)}')
        answer = prompt.string("Your answer: ")
        if (is_even(random_int) and answer == 'yes' 
            or not is_even(random_int) and answer == 'no'):
            print("Correct!")
        else:
            cur_answer = 'yes' if is_even(random_int) else 'no'
            print_wrong_answer(answer, cur_answer, name)

        count_tries -= 1
    print(f'Congratulations, {name}!')


def main() -> None:
    name = welcome_user()
    brain_even(name)
