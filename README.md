# A Day at Holy Cross

This game simulates a day as a student at Holy Cross. You choose when to wake up, what to eat, and how to spend the afternoon. Each event changes your energy. Class events and a number-guessing game add some randomness.

The goal is to finish the whole day with more than 40 energy points. Reaching 40 or less after any event ends the game in a loss when the game updates. 

## How to run

Keep these three Python files in the same folder:

- `ProjectDomenicYacovone.py`: starts the game and controls the day's sequence.
- `events.py`: contains the six events in the student's day.
- `game_helpers.py`: contains input validation and game-status functions.

With Python 3 installed, open a terminal in that folder and run it. 

Only Python's built-in `random` module is needed. 

## How to play

1. Enter your name. Empty names and names containing only ordinary spaces or tabs are rejected. Your starting energy is randomly chosen from 70 through 100, including both endpoints.
2. Choose whether to wake up or snooze. Waking up costs 5 energy. Snoozing adds 5 energy but has a 50% chance of making you late.
3. If you woke up on time, choose breakfast. If you are late, breakfast is skipped and you lose 20 energy.
4. Attend class. The program randomly chooses a pop quiz, movie, group work, lecture, presentation, or cancelled class. If you still have more than 40 energy, enter `1` to continue.
5. Choose lunch and an afternoon activity. Studying at the library costs 15 energy and sets up a useful clue from Maxim later.
6. If you have survived this far, guess Maxim's number from 0 through 10. If you studied, he tells you whether it is from 0 through 5 or from 6 through 10. Choose a number from the range displayed.
7. Choose how many energy points to gamble, from 0 through your current energy. A correct guess **adds twice the wager** to your current energy. A wrong guess subtracts the wager. A wager of 0 leaves your energy unchanged.
8. After the last event, finish with more than 40 energy to win.

For menus and wagers, type a number without spaces, leading zeros, or extra symbols, then press Enter. Invalid input produces another prompt. Wagers must be whole numbers; negative values and decimals are rejected.

## Player state and why these types fit

### Energy: an integer

`energy_level` stores the player's current score. All starting values, event changes, and wagers use whole points, so an integer represents the score directly. It supports exact addition, subtraction, and comparison with the 40-point losing boundary. Fractions are unnecessary because there are no parts of points. 

Each event receives the current energy as an argument and returns the updated value. The driver assigns that returned value back to `energy_level`. Passing and returning state makes it clear which event changed the score and avoids relying on a changing global variable.

The game does not cap energy at 100. A player can gain more than the starting maximum through good choices or a successful wager.

### Waking on time: a Boolean

`woke_up_on_time` is either `True` or `False`, matching the two possibilities: on time or late. `wake_up()` returns it along with energy. `eat_breakfast()` uses it to decide whether to offer food choices or apply the missed-breakfast penalty. A separate number or text label would add unnecessary possibilities to a two-state decision.

### Studying: a Boolean

`studied` is also a `True`/`False` value. It begins as `False` and becomes `True` when the player chooses to study. `after_class()` returns it with energy, and `guess_number()` receives it. This preserves a consequence of an earlier choice: studying costs energy now but earns a clue later. The clue improves the player's information without guaranteeing a correct guess.

### Determining the result

`check_game_status(energy_level)` returns `True` when energy is above 40 and `False` otherwise. During the day, the driver uses this result to decide whether another event can run.

At the end, `show_final_result()` calls `check_game_status()` and prints the win or loss message. This is a function calling another project function to determine the outcome from player state. A player with enough energy at that point has completed every event; a player who lost earlier has skipped the remaining events.

`wake_up()`, `go_to_class()`, and `guess_number()` each use randomness inside the function. The driver also randomly chooses starting energy. The same menu choices can therefore produce different outcomes in different games.

## Control flow

The driver runs the events in order: waking up, breakfast, class, lunch, afternoon activity, and Maxim's game. An energy check follows each event. If energy is 40 or less, the remaining events are skipped and the final result is a loss. Surviving every event leads to the final win message.

The `if`/`elif`/`else` statements select the effect of a player's choice or random event. Breakfast has an additional branch based on `woke_up_on_time`. The afternoon activity records `studied`, which controls whether Maxim gives a clue. A correct or incorrect guess then changes the score in different ways.

Class has a special pause: the player is asked to enter `1` only if the class event leaves enough energy to continue. Losing in class goes straight toward the loss result rather than asking the player to continue to lunch.

### Input-validation 

- Names: a loop requests another name when it is empty or contains only ordinary spaces, tabs, or the other listed blank characters. A character loop checks the submitted name.
- Menus: a `while` loop repeats until the text matches one of the allowed choices. The guessing menu uses the range from Maxim's clue when one is available.
- Wagers: a retry loop asks for a valid amount. A counting loop compares the submitted text with the permitted whole numbers from 0 through the current energy. A match supplies the accepted integer. If there is no match, the program asks again.

Wager validation uses loops, string comparisons, and whole-number arithmetic. It does not convert arbitrary input text to an integer. Letters, superscript digits, very long digit strings, decimals, and amounts outside the allowed range therefore produce another prompt rather than a conversion error.

Each retry has a valid input that lets the player continue. Entering a permitted choice or wager exits its validation loop, and entering a name containing a letter exits the name loop. No valid sequence of choices traps the player in a loop.

## Changes made

- Split the program into three files with separate driver, event, and helper.
- Put the driver sequence inside `main()` and added a final-result function that calls the status function.
- Reused menu-input helpers from multiple event functions.
- Validated blank names, menu choices, and wagers using loops and comparisons.
- Kept the losing value consistent: 40 or less loses.
- Added data validation to the Maxim game. 
- Removed the class continuation prompt when the player has already lost.
- Connected the study choice to a later clue from Maxim.

