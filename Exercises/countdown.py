x = int(raw_input("Choose a number to countdown from: "))
import time
while x >= 0 and x <= 20:
    print x
    x = x - 1
    time.sleep(1)
    if x < 0:
        print "BLASTOFF!"
    else:
        x = x
else:
    if x > 20:
        print "Put a value less than 20 please!"
    else:
        x = x