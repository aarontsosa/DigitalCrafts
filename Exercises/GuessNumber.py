import random
import time
Random = random.randint(1, 10) ## Random Number
x = 5 ## Guesses left
again = True ## Does the player want to play?

## Actual code of the Game##
print "Welcome Player to Guess a Number!"
time.sleep(.7) 
print "I am thinking of a number between 1 and 10\n"
while again == True:
    while x >= 0:
        if x > 0:                                           ## Check if player has any more guesses
            time.sleep(.7)
            print "\nYou have %d guesses left." % x
            guess = int(raw_input("What's your guess? "))
            if guess < Random:                              ## Check if the guess is too high
                time.sleep(.7)
                print "%d is too low." % guess
                x = x - 1
            elif guess > Random:                            ## Check if the guess is too low
                time.sleep(.7)
                print """%d is too high.""" % guess
                x = x - 1
            else:                                           ## If none, the guess is right
                time.sleep(.7)
                print "Yes! You win!\n\n"
                again = False
                x = (-1)
                time.sleep(.7)
        else:                                               ## Play has no more guesses
            print "\nSorry, you ran out of guesses.\n"
            again == False
            x = x - 1

## Does the player want to play again? ##
    again = raw_input("Do you want to play again?? " )
    again = again.lower()
    if again == "yes" or again == "y" or again == "sure" or again == "ok" or again == "okay":
        x = 5
        again = True
        Random = random.randint(1, 10)
    elif again == "n" or again == "no" or again == "nope" or again == "nah":
        again = False
        time.sleep(.7)
        print "\n\nGoodbye, and Thanks for Playing!\n"
    else:
        again = False
        time.sleep(.7)
        print "Goodbye, and Thanks for Playing!\n"