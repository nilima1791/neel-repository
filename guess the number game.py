# guess the number game
import random
print('Hello, Whats your name?')
name = input()
secretNumber =random.randint(1,20)
print('Well ,' + name +' I am thinking of a number between 1-20.')

for i in range (1,7):
    print('Take a guess')
    guess= int(input())
    
    if guess > 20 :
        print (' Please enter number between 1-20') # to make sure numbers b/w 1-20 are guessed 
    elif guess > secretNumber :
        print('Too high . Take another guess')
    elif guess < secretNumber:
        print('Too low . Take another guess')
    else :
        break # for when the guess is right .

if guess == secretNumber:
    print('Good Job!. It took you '+ str(i)+' chances to guess')
else :
    print('Nope, the number I was guessing was '+ str(secretNumber) +'. Better luck next time')
    
guess > 20 :
        print (' Please enter number between 1-20')
