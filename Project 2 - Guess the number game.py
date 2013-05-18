# "Guess the number" mini-project

# imports
import simplegui
import random

# global variables
secret_number = 0
limit = 0
case = 100

# helper function(s)

# to restart the game
def init():
    if (case == 100):
        range100()
    else:
        range1000()
    
    
# event handlers
    
def range100():
    global secret_number, limit, case
    case = 100
    
    # set the limit '7' for this case
    limit = 7
    
    # set the secret key for this range
    secret_number = random.randrange(0,100)
    
    print "New game. Range is from 1 to 100"
    print "Number of remaining guess is", limit
    print ""
    
def range1000():
    global secret_number, limit, case
    case = 1000
    
    # set the limit '10' for this case
    limit = 10
    
    # set the secret key for this range
    secret_number = random.randrange(0,1000)
    
    print "New game. Range is from 1 to 1000"
    print "Number of remaining guess is", limit
    print ""
    
def get_input(guess):
    global limit
    
    # convert the input from string to integer
    converted_guess = int(guess)
    
    # check condition between input number and random generated number
    if (limit > 0):        
        if (converted_guess == secret_number):
            result = "Correct!"
        elif (converted_guess < secret_number):
            result = "Higher!"
        else:
            result = "Lower!"
        
        # decrementing limit
        limit = limit - 1
        
        print "Guess was", converted_guess
        print "Number of remaining guesses is", limit
        print result	# print the result
        print ""		# print blank line
        
        # if result is correct, then restart the game
        if ( result == "Correct!" ):
            init()
            
    # case when not enough remaining guesses
    else:
        print "You ran out of guesses.  The number was", secret_number
        print ""
        init()
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements

# button for range100
frame.add_button("Range is [0 - 100)", range100, 200)	
# button for range1000
frame.add_button("Range is [0 - 1000)", range1000, 200)
# create input text box
frame.add_input("Enter a guess", get_input, 200)

# start frame
init()
frame.start()

