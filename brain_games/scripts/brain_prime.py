import random

import prompt

from brain_games.cli import print_wrong_answer, welcome_user
from brain_games.constants import ROUNDS_COUNT


def is_simple(num) -> str:
    if num < 2:
        return 'no'

    for i in range(2, num):
        if num % i == 0: 
            return 'no'
    return 'yes'

def brain_prime(name: str) -> None:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(ROUNDS_COUNT):
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')

        correct_answer = is_simple(random_number)

        answer = prompt.string('Your answer: ')

        if answer != str(correct_answer):
            print_wrong_answer(answer, correct_answer, name)
            return

        print('Correct!')

    print(f'Congratulations, {name}!')


def main() -> None:
    name = welcome_user()
    brain_prime(name)
