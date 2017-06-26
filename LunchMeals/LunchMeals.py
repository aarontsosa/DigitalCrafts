import time

def textLine(line):
    f = open(file, "r")
    return "".join([x for i, x in enumerate(f) if i == line])

file = "/Users/aaronsosa/DigitalCrafts-06-2017/python/LunchMeals/LunchMeals.txt"
f = open(file, "r")
firstTime = f.readline(4)
if firstTime == "True" :
    f = open(file,"w")
    f.write("False\n")
    print ("Welcome to Lunch Tracker")
    time.sleep(1)
    print ("Using this tracker you will keep track of where you have eaten for lunch here!")
    time.sleep(1)
    print ("First this is first, We need to know where you went today.")
else:
    f = open(file, "r")
    dayHolder = textLine(1)
    print ("Welcome Back! Last time you logged something was %s" % dayHolder )
f.close()
