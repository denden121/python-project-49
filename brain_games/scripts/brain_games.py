from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_even


def main() -> None:
    name = welcome_user()
    brain_even(name)
    

