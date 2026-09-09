import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def print_wrong_answer(
    answer: str,
    correct_answer: str | int,
    name: str,
) -> None:
    print(
        f"'{answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'.\n"
        f"Let's try again, {name}!"
    )
