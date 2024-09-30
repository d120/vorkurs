# This work is licensed under CC0 1.0 Universal Public Domain Dedication https://creativecommons.org/publicdomain/zero/1.0/
# https://en.wikipedia.org/wiki/Hangman_(game)

# This code was repeated multiple times so we extracted it into a method.
# This is an essential thing to make your code more readable.
# Checks whether `search_element` is contained in `search_list` while ignoring if it's upper or lowercase
def contains_ignore_case(search_list, search_element):
    for element in search_list:
        if element.lower() == search_element.lower():
            return True
    return False


secret_word = "Big Elefant"

guesses = 5
guess_nr = 1
already_guessed_letters = []

print('\n' * 1000)

while guess_nr <= guesses:
    print(f"Guess {guess_nr}/{guesses}\nThe word is: ")

    # build the string but hide characters that you haven't guessed yet
    guessed_word_string = ""
    for letter in secret_word:
        if letter == ' ':
            guessed_word_string += ' '
        elif contains_ignore_case(already_guessed_letters, letter):
            guessed_word_string += letter
        else:
            guessed_word_string += '_'
    print(guessed_word_string)

    guess = input("Guess a letter: ").lower()
    print('\n' * 1000)

    if len(guess) != 1:
        print("Guess exactly one letter")
        continue

    if contains_ignore_case(already_guessed_letters, guess):
        print("You already guessed that!")
        continue

    already_guessed_letters.append(guess)

    if contains_ignore_case(secret_word, guess):
        print(f"Nice guess!")
    else:
        guess_nr += 1
        print(f"That was wrong!")

    # check if the whole word got guessed
    done = True
    for letter in secret_word:
        if letter != ' ' and not contains_ignore_case(already_guessed_letters, letter.lower()):
            done = False

    if done:
        print(f"Nice job! You guessed the word! It was: {secret_word}")
        break

if not done:
    print(f"You're so bad! You can't even guess this simple word: {secret_word}")
