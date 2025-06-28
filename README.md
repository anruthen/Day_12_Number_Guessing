# Day 12 – Number Guessing Game 🎯

This project implements a number guessing game where the user plays against the computer. The user selects a difficulty level and tries to guess the randomly selected number within the given attempts.

## Features

- Console-based game with clear prompts
- Two difficulty levels: easy (10 attempts), hard (5 attempts)
- Random number between 1 and 100
- Feedback on whether the guess was too high or too low
- Game ends when the number is guessed or attempts run out

## How It Works

- The game picks a random number between 1 and 100.
- The player chooses the difficulty level.
- The player enters guesses one at a time.
- After each guess, feedback is given: too high, too low, or correct.
- The game ends with a win or loss message.

## Example Output
```
 ,----.                                      ,--.  ,--.                                          ,--.                  
'  .-./   ,--.,--. ,---.  ,---.  ,---.     ,-'  '-.|  ,---.  ,---.     ,--,--, ,--.,--.,--,--,--.|  |-.  ,---. ,--.--. 
|  | .---.|  ||  || .-. :(  .-' (  .-'     '-.  .-'|  .-.  || .-. :    |      \|  ||  ||        || .-. '| .-. :|  .--' 
'  '--'  |'  ''  '\   --..-'  `).-'  `)      |  |  |  | |  |\   --.    |  ||  |'  ''  '|  |  |  || `-' |\   --.|  |    
 `------'  `----'  `----'`----' `----'       `--'  `--' `--' `----'    `--''--' `----' `--`--`--' `---'  `----'`--'   

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty level. Type 'easy' or 'hard': hard
You have 5 guesses remaining.
What's your guess?: 50
You guessed too high.
You have 4 guesses remaining.
What's your guess?: 25
You guessed too high.
You have 3 guesses remaining.
What's your guess?: 10
You guessed too low.
You have 2 guesses remaining.
What's your guess?: 18
You guessed too low.
You have 1 guesses remaining.
What's your guess?: 23
You guessed too high.
You ran out of guesses. You lose!
```

## Skills Learned

- Understanding variable **scope** (local vs. global)
- Differences in **block scope** between Python and C++
- Use of **namespaces** in Python
- Naming conventions for constants (e.g., `MAX_ATTEMPTS`)
