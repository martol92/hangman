import random
from hangman_words import word_list  

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

display = []
outsideposition = 0

print(F"YOU HAVE {lives} LIVES")

for letter in chosen_word:
    display += "_"
#print("This is display at the beginning", display)
print("Guess the word", display)

while "_" in display and lives > 0:
    user_guess = input("Guess a letter: ")

    for position in range(word_length):
        outsideposition = position
        #print("This is position", position)
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = user_guess
            print(display[position])
            print(display)
            if "_" not in display:
                print("You win")


    if user_guess not in chosen_word:
        
        print(stages[lives])
        print("You just lost a life")
        lives -= 1
        print("Lives left: ", lives)
        if lives == 0:
            print("You lose")
            print(stages[lives])
            

