"""A number-guessing game."""

# Put your code here
import random

greeting = input("Howdy partner, what's your name? ")


def startGame():
    if greeting == 'Brant':
        randNum = random.randint(1,100)
        guess = int(input ('What number am I thinking of? '))
        tries = 1
        
        while guess != randNum:
            tries = tries + 1
            if guess > randNum:
                print('Your guess was', guess)
                guess = int(input('Your guess was too high, try again '))
            elif guess < randNum:
                print('Your guess was', guess)
                guess = int(input('Your guess was too low, try again '))
        while guess == randNum:
            print('Your guess was', guess)
            print('Good job! You guessed the number')
            print('Good job', greeting, 'you guessed the number in', tries, 'tries!')
            break

def main():
    startGame()

main()

# def startGame = input(greeting, " , I'm thinking a number between 1 and 100..can you guess what it is?")