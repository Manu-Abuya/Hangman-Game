# Import random and time libraries
import random
import time

# Steps to invite a user to the game
print("\n Welcome to Hangman Game \n")
name = input("Enter your name: ")
print("Hello " + name + ". Best of luck as you play!")
time.sleep(2)
print("The game is about to start!")
time.sleep(3)


def main():
    # declare global variables
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    # randomly choose a word
    words_to_guess = ["october", "benz", "cat", "girl", "movie", "child",
                      "stomach", "soda", "song", "spoil", "flower", "lorry", "country"]

    # assign to word
    word = random.choice(words_to_guess)

    # calculate the length of characters for every letter
    length = len(word)
    count = 0

    # print out some text on the screen
    display = '_' * length

    # create empty list that stores all of the guesses
    already_guessed = []
    play_game = ""

    # loop to execute the game when the first round ends
    def play_loop():
        global play_game
        play_game = input("Do you want to play again? y = yes, n = no \n")
        while play_game not in ["y", "n", "Y", "N"]:
            play_game = input("Do you want to play again? y = yes, n = no \n")
        # if "y", run main() and continue playing
        if play_game == "y":
            main()
        # if "n", print message
        elif play_game == "n":
            print("Thanks for playing! Come back again!")
        exit()

    # Initialize conditions for the game
    def hangman():
        global count
        global display
        global word
        global already_guessed
        global play_game
        limit = 5

        # Ask for a guess
        guess = input("This is the Hangman word: " +
                      display + "Enter your guess: \n")
        guess = guess.strip()

        if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= 9:
            print("Invalid Input, Try a placing a letter \n")
            hangman()

        # if correctly guessed, index searches for that letter
        elif guess in word:
            already_guessed.extend([guess])
            index = word.find(guess)
            word = word[:index] + "_" + word[index + 1:]
            # add letter in the given space according to the index
            display = display[:index] + guess + display[index + 1:]
            print(display + "\n")
        # if guessed already the correct letter, prints the message
        elif guess in already_guessed:
            print("Try another letter \n")

        # if guessed wrong, hangman tells us how many guesses are left
        else:
            # limit is set to , limit-count is the guesses left for the user
            count += 1
            if count == 1:
                time.sleep(1)
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) +
                      " guesses remaining \n")

            elif count == 2:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) +
                      " guesses remaining \n")

            elif count == 3:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) +
                      " guesses remaining \n")

            elif count == 4:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("Wrong guess. " + str(limit - count) +
                      " last guess remaining \n")
            elif count == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\ \n"
                      "  |    / \ \n"
                      "__|__\n")
                print("Wrong guess. You are hanged!!! \n")
                print("The word was:", already_guessed, word)
                play_loop()
        if word == '_' * length:
            print("Congrats! You have guessed the word correctly!")
            play_loop()
        elif count != limit:
            hangman()

    # Start again is the play_loop executes yes
    main()

    hangman()
