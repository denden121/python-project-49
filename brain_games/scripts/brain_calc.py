import random

import prompt

from brain_games.cli import print_wrong_answer, welcome_user
from brain_games.constants import ROUNDS_COUNT

OPERATORS = ('+', '-', '*')


def calculate(first_number: int, second_number: int, operator: str) -> int:
    if operator == '+':
        return first_number + second_number
    if operator == '-':
        return first_number - second_number
    if operator == '*':
        return first_number * second_number
    raise ValueError(f'Unsupported operator: {operator}')


def brain_calc(name: str) -> None:
    print('What is the result of the expression?')

    for _ in range(ROUNDS_COUNT):
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        operator = random.choice(OPERATORS)
        correct_answer = calculate(first_number, second_number, operator)

        print(f'Question: {first_number} {operator} {second_number}')
        answer = prompt.string('Your answer: ')

        if answer != str(correct_answer):
            print_wrong_answer(answer, correct_answer, name)
            return

        print('Correct!')

    print(f'Congratulations, {name}!')


def main() -> None:
    name = welcome_user()
    brain_calc(name)
