"""Handle the choices and energy changes during the student's day."""

import random

from game_helpers import check_game_status, get_valid_choice, get_valid_wager


def wake_up(energy_level):
    """
    Handle the player's morning choice and whether they wake up on time.

    Inputs:
      energy_level: integer; the player's current energy level
    Outputs:
      energy_level: integer; the player's updated energy level
      woke_up_on_time: Boolean; whether the player woke up on time
    Side effects:
      Print the morning choices and result, read a choice through a helper,
      and use a random number if the player snoozes.
    """
    print("\nYour alarm goes off at 8am for Intro to Python.")
    print("1. Wake up")
    print("2. Snooze")
    choice = get_valid_choice("Enter 1 or 2: ", ["1", "2"])

    if choice == "1":
        energy_level = energy_level - 5
        woke_up_on_time = True
    else:
        energy_level = energy_level + 5
        # Snoozing has a 50% chance of making the player late.
        chance = random.randint(1, 10)
        if chance <= 5:
            woke_up_on_time = True
        else:
            woke_up_on_time = False

    if woke_up_on_time:
        print("You woke up on time.")
    else:
        print("You woke up late.")

    print("Energy level:", energy_level)
    return energy_level, woke_up_on_time


def eat_breakfast(energy_level, woke_up_on_time):
    """
    Choose breakfast if the player woke up on time, or skip it if late.

    Inputs:
      energy_level: integer; the player's current energy level
      woke_up_on_time: Boolean; whether the player woke up on time
    Outputs:
      energy_level: integer; the player's updated energy level
    Side effects:
      Print the breakfast choices and result. Read a choice through a
      helper only if the player woke up on time.
    """
    print("\nBreakfast")

    if not woke_up_on_time:
        print("You have to skip breakfast because you are late.")
        energy_level = energy_level - 20
    else:
        print("1. Eat eggs and toast")
        print("2. Eat cereal")
        print("3. Skip breakfast")
        print("4. Eat oatmeal")
        print("5. Only have coffee :( ")
        choice = get_valid_choice(
            "Enter 1, 2, 3, 4, or 5: ", ["1", "2", "3", "4", "5"])

        if choice == "1":
            print("You eat eggs and toast.")
            energy_level = energy_level + 15
        elif choice == "2":
            print("You eat cereal.")
            energy_level = energy_level + 8
        elif choice == "3":
            print("You skip breakfast and lose energy.")
            energy_level = energy_level - 25
        elif choice == "4":
            print("You eat oatmeal.")
            energy_level = energy_level + 12
        else:
            print("You only have coffee.")
            energy_level = energy_level - 10

    print("Energy level:", energy_level)
    return energy_level


def go_to_class(energy_level):
    """
    Pick a random class event and change the player's energy.

    Inputs:
      energy_level: integer; the player's current energy level
    Outputs:
      energy_level: integer; the player's updated energy level
    Side effects:
      Use a random class event and print its result. Read a continuation
      choice through a helper only if the player can still continue.
    """
    print("\nClass")
    events = ["pop quiz", "movie", "group work", "lecture",
              "presentation", "cancelled class"]
    event = random.choice(events)

    if event == "pop quiz":
        print("You have a pop quiz today.")
        energy_level = energy_level - 20
    elif event == "movie":
        print("You watch a short film in class.")
        energy_level = energy_level + 7
    elif event == "group work":
        print("You do group work in class.")
        energy_level = energy_level - 12
    elif event == "lecture":
        print("You have a normal lecture in class.")
        energy_level = energy_level - 15
    elif event == "presentation":
        print("You have to give a presentation in class.")
        energy_level = energy_level - 25
    else:
        print("Your class gets cancelled.")
        energy_level = energy_level + 15

    print("Energy level:", energy_level)
    if check_game_status(energy_level):
        get_valid_choice("Enter 1 to continue to lunch: ", ["1"])

    return energy_level


def lunch(energy_level):
    """
    Let the player choose lunch and update their energy.

    Inputs:
      energy_level: integer; the player's current energy level
    Outputs:
      energy_level: integer; the player's updated energy level
    Side effects:
      Print the lunch choices and result, and read a choice through a
      helper.
    """
    print("\nLunch")
    print("1. Kimball Pizza")
    print("2. Kimball Salad Bar")
    print("3. Croads Sandwich")
    print("4. Kimball Fries")
    print("5. Kimball Burger <3")
    print("6. Croads bowl")
    print("7. Cupcake")
    choice = get_valid_choice(
        "Enter 1, 2, 3, 4, 5, 6, or 7: ",
        ["1", "2", "3", "4", "5", "6", "7"])

    if choice == "1":
        print("You eat pizza.")
        energy_level = energy_level - 15
    elif choice == "2":
        print("You eat a salad.")
        energy_level = energy_level + 10
    elif choice == "3":
        print("You eat a sandwich.")
        energy_level = energy_level + 12
    elif choice == "4":
        print("You eat fries.")
        energy_level = energy_level - 25
    elif choice == "5":
        print("You eat a burger.")
        energy_level = energy_level + 5
    elif choice == "6":
        print("You eat a rice bowl.")
        energy_level = energy_level + 15
    else:
        print("You eat a cupcake and feel tired after.")
        energy_level = energy_level - 30

    print("Energy level:", energy_level)
    return energy_level


def after_class(energy_level):
    """
    Choose an activity and remember whether the player studied.

    Inputs:
      energy_level: integer; the player's current energy level
    Outputs:
      energy_level: integer; the player's updated energy level
      studied: Boolean; whether the player chose to study at the library
    Side effects:
      Print the activity choices and result, and read a choice through a
      helper.
    """
    print("\nYou are bored after class, choose a fun activity.")
    print("1. Take a nap")
    print("2. Study at the library")
    print("3. Hang out with friends")
    print("4. Go to the gym")
    print("5. Go for a walk")
    print("6. Run a marathon")
    choice = get_valid_choice(
        "Enter 1, 2, 3, 4, 5, or 6: ", ["1", "2", "3", "4", "5", "6"])
    studied = False

    if choice == "1":
        print("You take a nap.")
        energy_level = energy_level + 5
    elif choice == "2":
        print("You study at the library.")
        print("Your studying will help you with Maxim's number game.")
        energy_level = energy_level - 15
        studied = True
    elif choice == "3":
        print("You hang out with friends.")
        energy_level = energy_level + 5
    elif choice == "4":
        print("You go to the gym.")
        energy_level = energy_level - 25
    elif choice == "5":
        print("You go for a walk.")
        energy_level = energy_level + 8
    else:
        print("You run a marathon.")
        energy_level = energy_level - 50

    print("Energy level:", energy_level)
    return energy_level, studied


def guess_number(energy_level, studied):
    """
    Let the player wager energy on guessing Maxim's random number.

    Inputs:
      energy_level: integer; the player's current energy level, above 40
      studied: Boolean; whether the player studied and should get a hint
    Outputs:
      energy_level: integer; energy after adding twice the wager for a
      correct guess or subtracting the wager for an incorrect guess
    Side effects:
      Use a random number. Print the rules, a hint if the player studied,
      the secret number after the wager, and the result. Read a guess and
      wager through helpers.
    """
    print("\nYour friend Maxim comes up to you before you head to bed.")
    print("He wants you to gamble your energy level points.")
    print("Pick a number between 0 and 10.")
    print("A correct guess adds twice your wager to your current energy.")
    print("A wrong guess subtracts your wager from your current energy.")
    print("You can wager 0 to keep all of your energy points.")
    random_number = random.randint(0, 10)
    valid_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    if studied:
        if random_number <= 5:
            print("Your studying helps: Maxim's number is between 0 and 5.")
            valid_numbers = ["0", "1", "2", "3", "4", "5"]
        else:
            print("Your studying helps: Maxim's number is between 6 and 10.")
            valid_numbers = ["6", "7", "8", "9", "10"]

    user_number = get_valid_choice("Enter your number: ", valid_numbers)
    user_number = int(user_number)
    print("You have", energy_level, "points able to be gambled.")
    points_gambled = get_valid_wager(energy_level)
    print("Maxim's number was", random_number)

    if random_number == user_number:
        energy_level = energy_level + (points_gambled * 2)
        print("You guessed Maxim's number and gained",
              points_gambled * 2, "energy points! :)")
    else:
        energy_level = energy_level - points_gambled
        print("You did not guess Maxim's number and lost",
              points_gambled, "energy points. :( )")

    print("Energy level:", energy_level)
    return energy_level
