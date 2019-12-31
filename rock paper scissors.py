# Rock paper scissor

import random
#create variable for computer and user
# Ask user input

def rps_game():
#------------ creating 2 variables for user and computer input --------------------------------------------------------------------------------------------------------

    user_input = input("what do you choose ? Rock, paper, Scissors?\n")
    computer = random.randint(1,3)
#------------ updating the user input to standard input ---------------------------------------------------------------------------------------------------------------    

    if user_input in ["Rock", "R","r","rock","ROCK"]:
       user_input ="rock"
    elif user_input in ["Paper","P","p","paper"]:
        user_input = "paper"
    elif user_input in ["Scissors","Scissor","SCISSOR","S","s"]:
        user_input = "scissor"
    else :
        print("Enter correct entry")
        rps_game()  
#--------------- converting random numbers selected by computer into variables rock paper and scissors ---------------------------------------------------------------

    if computer == 1 :
        computer = "rock"
    elif computer == 2 :
        computer = "paper"
    else :
        computer ="scissor"
#--------------------- plating the game --------------------------------------------------------------------------------------------------------------------------------
    if user_input == "rock" and (computer == "scissor" or computer == "paper"):
       print(user_input)
       print(computer)
       print ("user won")
    elif user_input == "scissor" and computer == "paper":
        print(user_input)
        print(computer)
        print ("user won")
    elif user_input == computer :
        print(user_input)
        print(computer)
        print("Its a draw")
    else :
        print(user_input)
        print(computer)
        print("computer won")
    game = input("Do you want to play again? Y/N")
    if game == "Y":
        rps_game()
    else:
        print("Thank you for playing")
    
rps_game()                     






