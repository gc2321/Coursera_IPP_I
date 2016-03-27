# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

num_range = 100
try_count = 7
number = 0

# helper function to start and restart the game
def new_game():
   #generate random integer
    global num_range, try_count, number
    number = random.randint(0, num_range)
    
    print (" ")
    print ("New Game. "+" Range is from 0 to "+str(num_range))  
    print ("Number of remaining guess is "+str(try_count))
    
# define event handlers for control panel
def range100():
    global num_range, try_count
    num_range = 100
    try_count = 7
    new_game()

def range1000():
    global num_range, try_count
    num_range = 1000
    try_count = 10
    new_game()
    
def get_input(guess):   
    global try_count, number
    guess = int(guess)
    
    print (" ")
    print ("Guess was "+str(guess))
    try_count -= 1
    
    if try_count!=0:      
        print ("Number of remaining guesses is "+str(try_count))
      
        if guess == number:
            print ("Correct!")
            range100()
        elif guess > number:
            print ("Lower!")
        elif guess < number:
            print ("Higher!")
    else:
        print ("You ran of guesses. The correct answer was "+str(number))
        range100()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# create buttons in windows
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", get_input, 200)

# call new_game 
f.start()
range100()
