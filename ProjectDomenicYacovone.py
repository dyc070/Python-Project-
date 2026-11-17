"""Play a Holy Cross student's day and finish above 40 energy points.

Run this file with events.py and game_helpers.py in the same folder.
"""

import random

from events import (
    after_class,
    eat_breakfast,
    go_to_class,
    guess_number,
    lunch,
    wake_up,
)
from game_helpers import (
    check_game_status,
    get_player_name,
    show_final_result,
)


def main():
    """Set up the player and run each event while energy stays above 40.

    Inputs: None. The called functions ask the player for their choices.
    Outputs: None.
    Side effects: Prints the story, reads input through other functions,
        and uses randomness for starting energy and the day's events.
    """
    name = get_player_name()
    energy_level = random.randint(70, 100)
    studied = False

    print("\nYou begin your day as a student at Holy Cross.")
    print(name + ", your starting energy level is", energy_level)
    print("Finish every event with more than 40 energy points to win.")
    print("At 40 or less, the game ends and you lose.")
    print("Studying costs energy but earns a hint for when talking to Maxim")

    energy_level, woke_up_on_time = wake_up(energy_level)

    if check_game_status(energy_level):
        energy_level = eat_breakfast(energy_level, woke_up_on_time)

    if check_game_status(energy_level):
        energy_level = go_to_class(energy_level)

    if check_game_status(energy_level):
        energy_level = lunch(energy_level)

    if check_game_status(energy_level):
        energy_level, studied = after_class(energy_level)

    if check_game_status(energy_level):
        energy_level = guess_number(energy_level, studied)

    
    show_final_result(name, energy_level)


if __name__ == "__main__":
    main()
