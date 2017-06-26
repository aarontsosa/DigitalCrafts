import time
file = "/Users/aaronsosa/DigitalCrafts-06-2017/python/LunchMeals/LunchMeals.txt"

def textLine(line):
    f = open(file, "r")
    return "".join([x for i, x in enumerate(f) if i == line])

def startUp():
    f = open(file, "r")
    firstTime = textLine(0)
    if firstTime != "False\n" :
        f = open(file,"a")
        f.write("False\n")
        print ("Welcome to Lunch Tracker")
        time.sleep(1.5)
        print ("Using this tracker you will keep track of where you have eaten for lunch here!")
        time.sleep(1.5)
        print ("First this is first, Lets get to know you!")
        time.sleep(1.5)
        return "newUsr"
    else:
        f = open(file, "r")
        dayHolder = textLine(2)
        name = textLine(1)
        print ("Welcome Back, %s! Last time you logged something was %s") % (name, dayHolder)
        return "oldUsr"

def name():
    name = raw_input("Let's start off easy. What's your first name? ")
    f = open(file, "a")
    f.write(name)
    f.write("\n")
    f.seek(0, 0)
    firstName = textLine(1)
    print "Awesome! Thanks %s" % firstName

def question(answer):
    answer = answer.lower()
    if answer == "yes" or answer == "y" or answer == "sure" or answer == "ok" or answer == "okay" or answer == "k":
        return "yes"
    elif answer == "no" or answer == "n" or answer == "nope" or answer == "none" or answer == "nah" or answer == "never":
        return "no"
    else:
        return answer

def manageRest():
    f = open(file, "r")
    oldRest = textLine(2)
    resturants = [ ]
    timesVisited = [ ]
    manageResturants = raw_input("Let's manage your resturants list. Would you like to add any resturants now? ")
    if question(manageResturants) == "yes":
        addRest = raw_input("What resturant do you want to add to your list? ")
        resturants.append(addRest)
        another = raw_input("Do you want to add another resturant to your list? ")
        while question(another) == "yes":
            addRest = raw_input("What else do you want to add to your list? ")
            resturants.append(addRest)
            another = raw_input("Do you want to add another resturant to your list? ")
        resturants = ", ".join(resturants)
        f = open(file, "a")
        f.write(resturants)
        f = open(file, "a")
        f.write("\n")
    resturants = list(resturants)
    length = len(resturants)
    for n in range(resturants):
        for z in 
    
def tracker():
    print resturants
    lunch = raw_input("Out of these which place did you eat today? ")
    f = open(file,"r")
    numVisited = textLine(4)
    placeHolder = 0
    popper = 0
    addition = 0
    timesVisited = [ ]
    for x in resturants:
        if lunch == x:
            addition = timesVisited[placeHolder] + 1
            placeHolder =+ 1
            timesVisited.insert(placeHolder, addition)
            timesVisited.pop(popper)
            popper =+ 1
            addition = 0
            break