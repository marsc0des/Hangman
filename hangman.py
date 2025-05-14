import random

def load_words(filename):
    """Load words from a file and return a list of words."""
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

def select_word(words):
    """Select a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed and others as underscores."""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    words = load_words("words.txt")  # Load words from file
    word = select_word(words)  # Select a random word
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()

