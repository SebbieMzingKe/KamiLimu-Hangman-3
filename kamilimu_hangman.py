import os
import random 
from words import words
import string

def get_valid_word(words):
    phrase = random.choice(list(words.keys()))
    # while '-' in phrase or ' ' in phrase:
    # phrase = random.choice(words)

    return phrase

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def hangman(words):

    phrases = list(words.keys())
    alphabet = set(string.ascii_uppercase)
    print("\nKamiLimu : _hellofriends. Guess any key phrase to access its information \n")

    while phrases:
        phrase = random.choice(phrases)
        word_letters = set(phrase) - {' '} # unique letters in the phrase excluding spaces
        used_letters = set() # keeps track of what user has guessed
        lives = 6


        while len(word_letters) > 0 and lives > 0:
            
            print("You have ", lives, " lives left and you have used these letters: ", " ".join(used_letters))

            word_list = [letter if letter in used_letters or letter == ' ' else "-" for letter in phrase]
            print("Current phrase: ", " ".join(word_list))

            user_letter = input('Guess a Letter :').upper()
    
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
            
                else:
                    lives = lives - 1
                    print(f"Letter {user_letter} is not in phrase.")

            elif user_letter in used_letters:
                print("You have already used that character. Please try a different one")

            else:
                print("Invalid character. Please try again.")


            clear_screen()
            if len(word_letters) > 0 and lives > 0:
                print("Enter another prompt:")

        if lives == 0:
            print("You died, sorry the phrase was ", phrase)
        else:
            print("Yay! you guessed the phrase ", phrase, "!! \n")
            for info in words[phrase]:
                print(f"- {info} \n")
            
            # if len(word_letters) == 0 and lives > 0:  # Clear screen only if phrase guessed correctly
            #     clear_screen()

            phrases.remove(phrase)
    print("Congratulations! You have guessed all the phrases ")
    print("\n200 OK")
hangman(words)
    



