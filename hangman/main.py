import random


def menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == "exit":
            exit()
        elif choice == "play":
            break


def game():
    words = ['python', 'java', 'kotlin', 'javascript']
    chosen_word = random.choice(words)
    letters = set(chosen_word)
    guessed_letters = set()
    tried_letters = set()
    tries = 8

    def validate(char):
        if not len(char) == 1:
            print("You should print a single letter")
            return False

        if not char.islower():
            print("It is not an ASCII lowercase letter")
            return False

        return True

    def print_word():
        word = chosen_word
        for char in chosen_word:
            if char not in guessed_letters:
                word = word.replace(char, '-')
        print(word)

    while tries > 0:
        print()
        if len(letters) == 0:
            print(chosen_word)
            print("You guessed the word!")
            print("You survived!")
            break

        print_word()
        letter = input("Input a letter: ")
        if not validate(letter):
            continue

        if letter in tried_letters:
            print("You already typed this letter")
            continue
        else:
            tried_letters.add(letter)

        if letter in letters:
            letters.remove(letter)
            guessed_letters.add(letter)
        else:
            tries -= 1
            print("No such letter in the word")
    else:
        print("You are hanged!")


print("H A N G M A N")
menu()
game()
