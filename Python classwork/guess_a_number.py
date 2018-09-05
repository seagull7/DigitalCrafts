import random 
def NumberGame():
    secret_num = random.randint(1, 10) 
    guess = int(input("I am thinking of a number between 1 and 10. What is it? \n"))
    count = 5
    while(count > 1):
        if (guess > secret_num):
            print (str(guess) + " is to high. ")
        elif(guess == secret_num):
            print("That's CORRECT!!!")
            break
        else:
            print (str(guess) + " is to low. ")
        count -= 1
        guess = int(input("You guessed wrong, try again! (you have " + str(count) + " guesses left.) \n\n"))

    again = raw_input("Do you want to play again? ('Y' or 'N')")
    if (again.upper() == "Y"):
        NumberGame()
    else:
        print ("Bye, then!")
NumberGame()