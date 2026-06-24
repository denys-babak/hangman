# hangman
This is a simple text-based Hangman game built in Python. The player must guess a randomly selected hidden word by entering letters or attempting to guess the entire word. Each incorrect guess costs one life, and after six mistakes, the game ends.

# 🎮 Hangman Game

A fun command-line Hangman game built with Python.

## 📖 Overview

Hangman is a classic word-guessing game where the player attempts to discover a hidden word one letter at a time.

At the start of the game, all letters in the selected word are hidden using underscores (`_`). The player can either:

* Guess one letter at a time
* Attempt to guess the entire word

Each incorrect guess adds a new part to the Hangman drawing. The player has **6 lives** before the game ends.

## ✨ Features

* Random word selection from a predefined word list
* Guess individual letters or the full word
* Tracks previously used letters
* Displays incorrect guesses
* Visual Hangman ASCII art progression
* Input validation
* Replay option after each game
* Exit the game anytime using `EXIT`

## 🎯 How to Play

1. Run the Python script.
2. A hidden word will be displayed as underscores.
3. Enter a letter to reveal matching characters.
4. Enter a full word if you think you know the answer.
5. Avoid making 6 incorrect guesses.
6. Win by revealing the entire word before the Hangman is completed.

### Example

Hidden word:

---

Guess:

A

Result:

_ A _ _ _ _

## 🛠 Requirements

* Python 3.x

No external libraries are required.

## ▶️ Running the Game

```bash
python hangman.py
```

## 📂 Word List

The game currently includes the following words:

* PLANET
* ORANGE
* CASTLE
* FOREST
* WINDOW
* PYTHON
* LETTER

You can easily add more words by editing the `answer_word_list` variable.

## 🎨 Hangman Stages

The Hangman drawing progresses through 6 stages, with a new body part added after each incorrect guess until the figure is complete.

## 📚 Concepts Used

This project demonstrates:

* Variables
* Lists
* Strings
* Loops (`while`)
* Conditional statements (`if`, `else`)
* User input handling
* Random selection (`random.choice`)
* Basic game logic
* ASCII art rendering

## 🚀 Future Improvements

Possible enhancements include:

* Larger word database
* Difficulty levels
* Categories (Animals, Countries, Movies, etc.)
* Score tracking
* Multiplayer mode
* Save high scores
* Colored terminal output
* Hint system

## 👨‍💻 Author

Created as a Python learning project to practice programming fundamentals and game development concepts.
