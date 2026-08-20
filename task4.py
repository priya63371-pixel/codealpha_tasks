import random

# List of words
words = ["python", "computer", "apple", "keyboard", "program"]

# Randomly choose a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:

    display = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if word is completed
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct!")
    else:
        attempts -= 1
        print("❌ Wrong!")
        print("Attempts left:", attempts)

# If attempts become zero
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)