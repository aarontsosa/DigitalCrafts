bill = float(raw_input("Hey! So what was the total bill? "))
service = raw_input("Okay, and how was the service? (Good, Fair, or Bad) ")
split = int(raw_input("How many ways are you spliting this? "))

if service == "Good":
    tipG = .2 * bill
    totalG = tipG + bill
    splitG = totalG / split
    print "Glad you had Good service"
    print "You're gonna leave them $%.2f" % tipG
    print "So, your total amount including tip will be $%.2f." % totalG
    print "Meaning, it's $%.2f per person" % splitG
elif service == "Fair":
    tipF = .15 * bill
    totalF = tipF + bill
    splitF = totalF / split
    print "Hope you had a good dinner."
    print "You're gonna leave them $%.2f" % tipF
    print "So, your total amount including tip will be $%.2f." % totalF
    print "Meaning, it's $%.2f per person" % splitF
elif service == "Bad":
    tipB = .1 * bill
    totalB = tipB + bill
    splitB = totalB / split
    print "Sorry about the bad service"
    print "You should at least leave them $%.2f" % tipB
    print "So, your total amount including tip will be $%.2f." % totalB
    print "Meaning, it's $%.2f per person" % splitB     
else:
    print "Not a valid responce."