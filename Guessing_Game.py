import random

lives = 5
words = ['airplane', 'scissors', 'treasure', 'syllable', 'magnolia', 'strength', 'business']
hidden_word = random.choice(words)
clues = list('????????')


def update_clue(guessed_letter, hidden_word, clues): #Changes the '?' in the list to the letter guessed by the user
    index = 0
    while index < len(hidden_word):
        if guessed_letter == hidden_word[index]:
            clues[index] = guessed_letter
        index = index + 1


while lives > 0:
    print(clues)
    print('Lives left: ' + str(lives))
    guess = input('Enter a letter or the whole word: ')

    if guess == hidden_word: #When the user guesses the whole word
        print("You've won! The hidden word was " + hidden_word)
        break

    if guess in hidden_word: #When the user enters a letter
        update_clue(guess, hidden_word, clues)
    else:
        print('Incorrect! You lost a life. Try again.')
        lives = lives - 1

    if lives == 0:
        print("Tough luck! The hidden word was " + hidden_word)
        break
