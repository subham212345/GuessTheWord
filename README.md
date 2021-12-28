# GuessTheWord

The goal of the project is to create "Guess The Word" game using Python, where the user can specify the number of attempts they want. Every time the user is able to guess a letter
that is present in the word, the console displays the position of the gussed letter while marking all other un-guessed letters as "_" mark. If the user guesses a wrong letter,
the console displays the number of attempts left.

The project uses the file "words.py" as a source of words for the game, which provides a number of words as a list.

# Random

The project makes use of the Random module.
The python module implements pseudo-random number generators for various distributions.

In this project, the "random.choice()" function is used to pick a random word from the list of words derived from the Words.py file.
