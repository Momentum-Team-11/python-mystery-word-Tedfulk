import random


def play_game():
    # print("Hello Teddy")
    with open("test-word.txt") as file:
        text_words = file.read()
        global words
        words = list(map(str, text_words.split()))
        the_words = random.choice(words)
        count = len(the_words)
        easy = 1, 2, 3, 4
        normal = 5, 6, 7
        hard = 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
        intro = input(
            "Would you like to play a 4 letter game? [y/n] ")
        if intro == "y":
            intro2 = input("Which level would you like to play? (1, 2, 3) ")
            print("Your word is", len(the_words), "letters long")
        if intro == "n":
            print("Okay, have a nice day!")
            exit()
        all_guesses = []
    while count > 0:
        if intro2 == "1":
            count = count - 1
            guesses = input(
                "Guess one letter at a time. Make your guess: ")
        print([letter if letter in guesses else "_" for letter in the_words])
        print("You have", count, "guesses left.")
        if count > len(the_words):
            print("GAME OVER no guesses left :(")
            break


if __name__ == "__main__":
    play_game()
