import random
from colorama import Fore, Back, Style
from colorama import init
init()

the_word = ""


def play_game():
    global the_word
    with open("words.txt") as file:
        text_words = file.readlines()
    words = [word.upper().strip() for word in text_words]
    count = 8
    diction = dict()
    for w in words:
        diction[w] = len(w)
    intro = input(
        "Would you like to play hangman? [y/n] ").casefold()
    if intro == "y":
        intro2 = input("Which level would you like to play? (1, 2, 3) ")
    if intro2 == "1":
        the_word = random.choice(
            list({k: v for (k, v) in diction.items() if v >= 3 and v <= 5}))
    elif intro2 == "2":
        the_word = random.choice(
            list({k: v for (k, v) in diction.items() if v >= 6 and v <= 8}))
    elif intro2 == "3":
        the_word = random.choice(
            list({k: v for (k, v) in diction.items() if v >= 9}))
    print(f"Your word is", {len(the_word)}, "letters long")
    if intro == "n":
        print("Okay, have a nice day!")
        exit()
    incorrect_guesses = []
    display = ["_"] * len(the_word)
    while count > 0:
        i = 0
        if "_" not in display:
            print(Fore.GREEN + "Congrats, you guessed the word." + Fore.RESET)
            quit()
        guess = input(
            "Guess one letter at a time. Make your guess: ").upper()
        if len(guess) != 1:
            print(Fore.RED + "Please only use 1 character." + Fore.RESET)
        elif guess in incorrect_guesses:
            print(Fore.RED + "Your letter was already guessed." + Fore.RESET)
        elif guess in the_word:
            for letter in the_word:
                if letter == guess:
                    display[i] = letter
                i += 1
            print(display)
        else:
            incorrect_guesses.append(guess)
            count = count - 1
            print(incorrect_guesses)
            print(Fore.YELLOW + "Incorrect you have",
                  count, "guesses left." + Fore.RESET)
    print(Fore.RED +
          "GAME OVER no guesses left :( the correct answer is {}.".format(the_word))
    return the_word


if __name__ == "__main__":
    play_game()
