######## N TO M ########
# i = int(raw_input("What number would you like to start on? "))
# x = int(raw_input("What number would you like to end on? "))
# while i <= x:
#   print i
#   i = i + 1

####### ANOTHER COIN #######
# i = True
# x = 0
# while i == True:
#     print "You have %d coins" % x
#     another = raw_input("Do you want another? ")
#     i = (another == "yes" or another =="YES" or another == "Yes")
#     if i == True:
#         x = x + 1
#     else:
#         print "Goodbye"

###### PRINT A SQUARE 1 AND 2 #########
# x = 0
# y = int(raw_input("How big do you want to make the square? "))
# while x <= y:
#     print "*" * y
#     x = x + 1

######## PRINT A BOX ########
# w = int(raw_input("Width? "))
# h = int(raw_input("Height? "))
# x = w + h
# y = 1
# s = w - 2
# while y <= x:
#     if y == h:
#         print "* " * w
#         y = y + 1
#         break
#     elif y == 1:
#         print "* " * w
#         y += 1
#     else:
#         print "* " + "  " * s + "*"
#         y = y + 1

########## PRINT A TRIANGLE 1 AND 2 #######
# h = int(raw_input("Height? "))
# def starTriangle(height):
#     x = 1
#     s = 0
#     y = height + (height - 1)
#     import math
#     math.floor(s)
#     while y >= 1:
#         s = y / 2
#         math.floor(s)
#         print " " * s + "*" * x + " " * s
#         x = x + 2
#         y = y - 2
        
# starTriangle(h)

######### MULTIPLICATION TABLE ##########
# f = 1
# s = 1
# x = 1
# while x <= 10:
#     if s <= 10:
#         p = f * s
#         print "%d X %d =" % (f, s),
#         print p
#         s = s + 1
#     else:
#         f = f + 1
#         x = x + 1
#         s = 1

########## PRINT A BANNER #########
# text = raw_input("Text? ")
# size = len(text)
# x = 1
# y = size + 4
# while x <= 3:
#     if x == 1 or x == 3:
#         print "*" * y
#         x = x + 1
#     else:
#         print "* " + text + " *"
#         x = x + 1

############ Triangle Numbers ##########
# x = 1
# while x <= 100:
#     num = (x * (x + 1)) / 2
#     print num
#     x = x + 1

########### FACTOR OF A NUMBER ########
num = (int(raw_input("Which number do you want to know the factor of? ")))
def factorOf(num):
    goTill = num + 1
    x = [ ]
    for i in range(goTill):
        for j in range(goTill):
            result = i * j
            if result == num:
                x.append("%d X %d = %d\n" % (i, j, num))
    return "".join(x)

print factorOf(num)