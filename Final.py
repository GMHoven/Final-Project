#-------------------------------------------
# Name: Week 15 Final project
#
#  Author: Grant Hoven
#------------------------------------------------
import random #Importing Random Number Generator 
file = open("words.txt").readlines() #Opeing the Word list text file
WordList = file[0].split(", ") #Separating all the words 
def GetRandomWord(): 
    RandomIndex = random.randint(0,99) #Pick random number from  0-99
    return WordList[RandomIndex] #picking corresponding word in list 

def Wordle():
    CorrectWord = GetRandomWord() #Grabbing random word
    PlayerWin = False # Setting up win/loss condition
    GuessCounter = 0 # Tracks which guess count player is on 
    for GuessCounter in range(1,7): #loop 6 times
        print("Guess " + str(GuessCounter) + "/6") # Printing guess number 
        WordGuess = "" #sets up user guess 
        while len(WordGuess) != 5: # Loops until player guess is 5 letters
            WordGuess = input("Please enter a 5 letter word:") #ask for input 
            if len(WordGuess) != 5: #checking guess lenght 
                print("Guess is not 5 letters")
        GuessedCorrectly = CheckGuess(WordGuess,CorrectWord) #check if guess matches the correct word
        if GuessedCorrectly:
            PlayerWin = True 
            break # Stops guessing loop
    if PlayerWin == True:
        print("Good Job! You got the correct word in " + str(GuessCounter) + " guesses.")
    elif PlayerWin == False:
        print("Game Over. The correct word was " + CorrectWord + ".")

def CheckGuess(Guess,Correct):
    for i in range(0,5): 
        if Guess[i].upper() == Correct[i].upper(): #Checking for green letter. .upper() is used for comparisons so that capital and lowercase inputs are treated the same
            print(" \033[42m "+ Guess[i].upper() + " \033[40m", end="")  # Colors were found online. \033[42m is a green background, \033[40m Changes text back to white 
        elif Guess[i].upper() in Correct.upper(): #Checking for yellow letter
           print(" \033[43m "+ Guess[i].upper() + " \033[40m", end="") #\033[43m is a yellow background
        else: # Red letter if not yellow or green
            print(" \033[41m "+ Guess[i].upper() + " \033[40m", end="") # \033[41m is a red background 
    print("") # aligns text
    if Guess.upper() == Correct.upper():
        return True # function returns true if guess matches correct word 
    else:
        return False
    
def Gameloop(): # This is the game loop function 
    KeepPlaying = True
    print("Welcome to Wordle. Try to guess the 5 letter word in 6 or fewer guesses.")
    while KeepPlaying: # game loops until KeepPlaying is false 
        Wordle() 
        while True: # loops until Yes or no is entered 
            PlayAgain = input("Would you like to play again? (Yes or No)")
            if PlayAgain.upper() == "YES":
                break
            elif PlayAgain.upper() == "NO": 
                print("Thank you for playing.")
                KeepPlaying = False
                break
            else:
                pass

Gameloop() # run game


#Unit testing. Uncomment to test.
#assert CheckGuess("Grave","Spare") == False 
#assert CheckGuess ("Apple","Apple") == True

