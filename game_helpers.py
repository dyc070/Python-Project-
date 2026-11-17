"""Handle player input, energy checks, and the final game result."""


def get_player_name():
    """Ask for a name that contains at least one nonblank character.

    Inputs: None.
    Outputs: The player's name as a string.
    Side effects: Reads keyboard input and prints validation messages.
    """
    valid_name = False

    while not valid_name:
        name = input("Enter your name: ")

        for character in name:
            if character not in [" ", "\t", "\n", "\r", "\v", "\f"]:
                valid_name = True

        if not valid_name:
            print("Please enter a name.")

    return name


def get_valid_choice(prompt, valid_choices):
    """Keep asking until the player enters one of the allowed choices.

    Inputs: prompt, a string; valid_choices, a list of allowed strings.
    Outputs: The player's valid choice as a string.
    Side effects: Reads keyboard input and prints validation messages.
    """
    choice = input(prompt)

    while choice not in valid_choices:
        print("That choice is not available. Use the numbers shown.")
        choice = input(prompt)

    return choice


def get_valid_wager(energy_level):
    """Ask for a whole-number wager within the player's available energy.

    Inputs: energy_level, a nonnegative integer.
    Outputs: An integer from 0 through energy_level, including both ends.
    Side effects: Reads keyboard input and prints validation messages.
    """
    valid_wager = False

    while not valid_wager:
        points_text = input(
            "Enter points to gamble, from 0 to " + str(energy_level) + ": "
        )
        candidate = 0

        # Compare with allowed numbers without converting the player's text.
        while candidate <= energy_level and points_text != str(candidate):
            candidate = candidate + 1

        if candidate <= energy_level:
            valid_wager = True
        else:
            print("Use a whole number without spaces or zeros in front.")
            print("The gambled wager cannot be negative or exceed your energy level :/ .")

    return candidate


def check_game_status(energy_level):
    """Check whether the player has enough energy to continue.

    Inputs: energy_level, the player's current energy as an integer.
    Outputs: True for energy above 40, or False for energy at 40 or less.
    Side effects: None. True means a win only after the final event.
    """
    if energy_level > 40:
        return True
    else:
        return False


def show_final_result(name, energy_level):
    """Check the player's state and display the completed game's result.

    Inputs: name, a string; energy_level, the final energy as an integer.
    Outputs: None.
    Side effects: Prints the result and final energy. Call only after the
        day finishes or the player loses enough energy to end the game.
    """
    if check_game_status(energy_level):
        print("\n" + name + ", you made it through the day. You win!")
    else:
        print("\n" + name + ", your energy is too low. You lose.")

    print("Final energy:", energy_level)
    print("The game ends.")
