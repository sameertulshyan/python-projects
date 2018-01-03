#Simple implementation of hangman in python, using the command line interface
#Contains a text file with a bank of words to play the game with

import random

def choose_word(file_name):
        file_text = open(file_name, 'r')
        wordlist = file_text.readlines()
        word = wordlist[random.randint(0, len(wordlist) - 1)].replace('\n','')
        return str(word)

print("Welcome to the hangman game!")
word = choose_word('words.txt')
guesses = []

for i in range(len(word)):
        guesses.append('_ ')

print(''.join(guesses))

incorrect_guesses = []

while (len(incorrect_guesses) < 6):

        if '_ ' not in guesses:
                print('\nCongratulations! You win!')
                break

        guess = str(input('\nGuess a letter: '))
                
        if guess in word:  
                for c in range(len(word)):
                        if guess == word[c]:
                                guesses[c] = guess + ' '
                print('Updated word: ' + ''.join(guesses))
                print('\n' + 'Incorrect guesses: ' + ''.join(incorrect_guesses))
        else:
                if len(incorrect_guesses) == 5:
                        print('Game over!')
                        print('The word was: ' + str(word))
                else:
                        print('Wrong! You have ' + str(5 - len(incorrect_guesses)) + ' guesses left')
                        incorrect_guesses.append(guess)
                        print('Updated word: ' + ''.join(guesses))
                        print('\n' + 'Incorrect guesses: ' + ''.join(incorrect_guesses))
