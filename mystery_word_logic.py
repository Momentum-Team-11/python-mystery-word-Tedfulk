import random


def play_game():
    with open("test-word.txt") as file:
        text_words = file.read()
    words = list(map(str, text_words.split()))
    the_word = random.choice(words)
    count = 8

    # normal =
    # hard =
    intro = input(
        "Would you like to play a word game? [y/n] ")
    if intro == "y":
        intro2 = input("Which level would you like to play? (1, 2, 3) ")
        # if intro2 == 1:
        #     len(the_word).range(5)
        # if intro2 == 2:
        #     len(the_word) <=
        # if intro2 == 3:
        #     len(the_word) <= 4
        print("Your word is", len(the_word), "letters long")
    if intro == "n":
        print("Okay, have a nice day!")
        exit()
    incorrect_guesses = []
    display = ["_"] * len(the_word)
    while count > 0:
        if "_" not in display:
            print("Congrats, you guessed the word.")
            quit()
        if intro2 == "1":
            guess = input(
                "Guess one letter at a time. Make your guess: ").casefold()
            # print([letter if letter in guesses else "_" for letter in the_words])
        i = 0
        if len(guess) != 1:
            print("Please only use 1 character.")
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
            print("You have", count, "guesses left.")
    print("GAME OVER no guesses left :( the correct answer is {}.".format(the_word))


def difficulty():
    pass


if __name__ == "__main__":
    play_game()
