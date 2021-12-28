from words import word_list
import random

attempts = int(input("Enter the number of attempts you would like: "))

word_to_guess = random.choice(word_list)

print(word_to_guess)
word_len = len(word_to_guess)

display = []
for n in range(word_len):
    display += "_"

not_guessed = True

while not_guessed:
    user_guess = input("Guess a letter: ").lower()
    if user_guess in display:
        print("Already guessed")
    for position in range(word_len):
        letter = word_to_guess[position]
        if letter == user_guess:
            display[position] = letter

    if user_guess not in word_to_guess:
        attempts -= 1
        print(f"You guessed {user_guess}, that's not in the word. You have {attempts} attempts left.")

        if attempts == 0:
            not_guessed = False
            print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        not_guessed = False
        print("You win.")




