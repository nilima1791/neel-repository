import random

import sys 

user_input = "Y"   

while user_input == "Y"  :
    dice = random.randint(0,6)
    print("Welcome to the game . \nThe dice number is ...\n", dice)
    print("do you want to play again")
    user_input = input()
    if user_input =="N":
        print("Thank you for playing :) ")
        sys.exit
    elif user_input != "Y" or "N":
        print("enter correct alphabet . Y/N")
        user_input = input()
    
