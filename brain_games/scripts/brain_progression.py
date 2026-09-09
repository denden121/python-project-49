import random

import prompt

from brain_games.cli import print_wrong_answer, welcome_user

PROGRESSION_LENGTH = 10
ROUNDS_COUNT = 3


def make_progression(start: int, step: int) -> list[int]:
    return [start + step * index for index in range(PROGRESSION_LENGTH)]


def brain_progression(name: str) -> None:
    print('What number is missing in the progression?')

    for _ in range(ROUNDS_COUNT):
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)
        progression = make_progression(start, step)
        correct_answer = progression[hidden_index]
        question = [str(number) for number in progression]
        question[hidden_index] = '..'

        print(f"Question: {' '.join(question)}")
        answer = prompt.string('Your answer: ')

        if answer != str(correct_answer):
            print_wrong_answer(answer, correct_answer, name)
            return

        print('Correct!')

    print(f'Congratulations, {name}!')


def main() -> None:
    name = welcome_user()
    brain_progression(name)
