import random

import prompt

from brain_games.cli import print_wrong_answer, welcome_user

ROUNDS_COUNT = 3


def find_gcd(first_number: int, second_number: int) -> int:
    while second_number != 0:
        first_number, second_number = (
            second_number,
            first_number % second_number,
        )
    return abs(first_number)


def brain_gcd(name: str) -> None:
    print('Find the greatest common divisor of given numbers.')

    for _ in range(ROUNDS_COUNT):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        correct_answer = find_gcd(first_number, second_number)

        print(f'Question: {first_number} {second_number}')
        answer = prompt.string('Your answer: ')

        if answer != str(correct_answer):
            print_wrong_answer(answer, correct_answer, name)
            return

        print('Correct!')

    print(f'Congratulations, {name}!')


def main() -> None:
    name = welcome_user()
    brain_gcd(name)
