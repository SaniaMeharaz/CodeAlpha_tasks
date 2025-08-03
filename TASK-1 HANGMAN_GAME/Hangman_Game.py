import random
words = ['apple', 'robot', 'dream', 'plant', 'house']
secret_word = random.choice(words)
guessed_letters = []  
tries_left = 6         
print("Welcome to Hangman!")
print("Guess the word letter by letter.")
while tries_left > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word.strip())
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 You guessed the word! You win!")
        break
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    if guess in secret_word:
        guessed_letters.append(guess)
        print("✅ Correct!")
    else:
        tries_left -= 1
        print(f"❌ Wrong! {tries_left} tries left.")
if tries_left == 0:
    print("\n😢 You ran out of guesses. The word was:", secret_word)
