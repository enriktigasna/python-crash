# Crash Game

## Overview

The "Crash Game" is a simple command-line-based game where the player places a bet and attempts to cash out before the game crashes. The crash point is determined by a random multiplier calculated using a cryptographic hash function.

## Features

- **Balance:** The player starts with a balance of 100 units.
- **Betting:** The player can input the amount they want to bet from their balance.
- **Multiplier:** The game calculates a random multiplier using a cryptographic hash function.
- **Cash Out:** The player can choose to cash out at any point before the game crashes.
- **Result:** The player's return is determined by the chosen cash-out point.

## How to Play

1. Run the script in a Python environment.
2. Enter the amount you want to bet (integer only).
3. Monitor the current multiplier and return.
4. Press `SPACE` and then `ENTER` to cash out at the desired multiplier.
5. If the game crashes before you cash out, you lose the bet.

## Code Structure

- `get_hash()`: Generates a random hash for calculating the multiplier.
- `calculate_result()`: Calculates the game result based on the hash and determines if the game crashes.
- `read_input()`: Reads user input with a timeout, allowing the player to cash out.
- `play_round()`: Manages the gameplay, including betting, monitoring multipliers, and determining returns.
- Main game loop: Repeatedly prompts the user for bets and plays rounds until the player decides to exit.

## Constants

- `BALANCE_START`: The initial balance for the player.
- `E`: A constant used in multiplier calculation.
- `SALT`: A constant salt value for enhancing hash security.
- `TIMEOUT`: The time window for the player to make decisions.

## Dependencies

- Python 3.x

## Inspiration

This implementation was inspired by the YouTube video [Creating a Crash Game in Python](https://www.youtube.com/watch?v=F1HA7e3acSI). Special thanks to the video creator for providing the inspiration and insights.

## Usage

1. Install Python on your system.
2. Run the script in a terminal or command prompt.
3. Follow on-screen instructions to place bets and cash out.

## Example

```bash
$ python crash_game.py
How much do you want to bet? Your current balance is 100.
```

## Notes
- Ensure that you have Python installed on your machine.
- This is a basic implementation and can be extended for more features and interactivity.
