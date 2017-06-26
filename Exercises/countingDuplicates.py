###### UpperCase String ########
# google = "hello"
# print google.upper()

####### Capitalize a String ######
# print google.capitalize()

####### Reverse a String ##########
#print google[::-1]

###### LeetSpeak #######
# leet = raw_input("What do you want to translate into leet? ")
# leet = leet.upper()
# leet = list(leet)
# length = len(leet)
# trans = {
#     "A": "4","B": "B","C":"C","D":"D","E":"3","F":"F","G":"6","H":"H","I":"1","J":"J","K":"K","L":"L","M":"M",
#     "N":"N","O":"0","P":"P","Q":"Q","R":"R","S":"5","T":"7","U":"U","V":"V","W":"W","X":"X","Y":"Y","Z":"Z",
#     " ":" ","\'":"\'",".":".",",":",",":":":","?":"?","!":"!"
# }                                                                                                                         ## Used if you want to make your own code
# x = [ ]                                                                                                                   ## The new list for the translated code
# y = 0                                                                                                                     ## What moves the counter across the array
# z = len(leet)
# while y < length:
#     x.append(trans[leet[y]])
#     y = y + 1
# print "".join(x)

##### Long-long Vowels #######
# vowel = raw_input("What do you want to elongate? ")
# vowel = list(vowel)
# length = len(vowel)
# x = 0                                                    ##First Number you compare with
# y = 1                                                    ##Second Number you compare with
# z = 1                                                    ##Used for times to repeat while loop
# while y <= length:
#     if vowel[y] == vowel[x]:                             ##If it finds a match, add the extra letters
#         while z <= 3:
#             vowel.insert(y, vowel[y])
#             z = z + 1
#         x = x + 4
#         y = y + 4
#         z = 1
#     else:                                                ##If it does not, it will keep moving along
#         x = x + 1
#         y = y + 1
# print "".join(vowel)                                     ##Print what it found

######## Sum the Numbers ########
# num = [5, 5]
# length = len(num)
# x = 0
# y = 1
# z = num[x] + num[y]
# print z

########## Largest Number ##########
# num = [5, 3, 1, 20, 7, 3, 13, 8, 4, 3, 8]
# length = len(num)
# counter = 1
# largest = num[0]
# while counter < length: 
#     if largest < num[counter]:
#         largest = num[counter]
#         counter = counter + 1
#     else:
#         counter = counter + 1
# print largest

####### Smallest Number ##############
# num = [5, 3, 20, 7, 3, 13, 8, 4, 3, 8]
# length = len(num)
# counter = 1
# smallest = num[0]
# while counter < length: 
#     if smallest > num[counter]:
#         smallest = num[counter]
#         counter = counter + 1
#     else:
#         counter = counter + 1
# print smallest

######## Even Numbers ##############
# num = [5, 3, 20, 7, 3, 13, 8, 4, 3, 8, 2]
# length = len(num)
# counter = 0
# finder = 0
# even = [ ]
# while counter < length:
#     finder = num[counter] % 2
#     if finder == 0:
#         even.append(num[counter])
#         counter = counter + 1
#     else:
#         counter = counter + 1
# print even

########## Positive Numbers 1 and 2 ##########
# num = [5, 3, 20, 7, 3, 13, 8, 4, 3, 8, 2, -1]
# length = len(num)
# counter = 0
# finder = num[counter]
# positive = [ ]
# while counter < length:
#     finder = num[counter]
#     if finder > 0:
#         positive.append(num [counter])
#         counter = counter + 1
#     else:
#         counter = counter + 1
# print positive

############### Multiply a List ##############
# num = [3, 4, 5]
# factor = [3]
# product = 0
# end = [ ]
# counter = 0
# while counter < len(num):
#     product = num[counter] * factor[0]
#     end.append(product)
#     counter = counter + 1
# print end

############ Multiply Vectors ############
# num = [3, 4, 5]
# factor = [3, 4, 5]
# product = 0
# end = [ ]
# counter = 0
# while counter < len(num):
#     product = num[counter] * factor[counter]
#     end.append(product)
#     counter = counter + 1
# print end

############# Matrix Additon #############
# num = [[1, 3], 
#        [2, 4]]
# num2 = [[5, 2],
#         [1, 0]]
# result = [[0, 0], [0, 0]]
# for i in range(len(num)):
#     for j in range(len(num[0])):
#         result[i][j] = num[i][j] + num2[i][j]
# for r in result:
#     print (r)

# ############# Matrix Addition 2 #############
# num = [[1, 3], 
#        [2, 4]]
# num2 = [[5, 2],
#         [1, 0]]
# result = [[num[i][j] + num2[i][j] for j in range(len(num[0]))] for i in range(len(num))]

# for r in result:
#     print r

############ De-dup #############
# text = raw_input("What do you want to de-dup? ")
# text = list(text)
# counter = -1
# end = [ ]
# for i in text:
#     if i == text[counter]:
#         counter +=1
#     else:
#         end.append(i)
#         counter +=1
# print "".join(end)

########## Caesar Cipher ############ NOT DONE!
# code = raw_input("What do you want to turn into a Cesar Cypher? ")
# code = code.lower()
# code = list(code)
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphabet = list(alphabet)
# counter = int(raw_input("By how many do you want to change it by? "))
# decipher = 0
# ogplace = 0
# end = [ ]
# while decipher < len(code):
#         if counter < 26:
#             for i in code:
#                 decipher +=1
#                 ogplace = 0
#                 for h in alphabet:
#                     if i == " ":
#                         end.append(" ")
#                         break
#                     elif i != h:
#                         ogplace +=1
#                     else: 
#                         ogplace = ogplace + counter
#                         if ogplace < 26:
#                             end.append(alphabet[ogplace])
#                             break
#                         else:
#                             ogplace = ogplace - 25
#                             end.append(alphabet[ogplace])
#                             break
#         else:
#             counter = counter - 25
# print "".join(end)

# def find_missing_letter(chars):
#     x = 0
#     y = 0
#     alphabet = list("abcdefghijklmnopqrstuvwxyz")
#     go = True
#     stop = False
#     for i in chars:
#         while go == True:
#             for j in alphabet:
#                 if i == j:
#                     go = False
#                     break
#                 else:
#                     x += 1
#         else:
#             break
#     while stop == False:
#         if alphabet[x] == chars[y]:
#             x += 1
#             y += 1
#         else:
#             print alphabet[x]
#             stop = True

#print find_missing_letter(['a','b','c','d','f'])

# def find_missing_letter(chars):
#     chars = chars.lower()
#     x = 0
#     y = 0
#     alphabet = list("abcdefghijklmnopqrstuvwxyz")
#     go = True
#     stop = False
#     for i in chars:
#         while go == True:
#             for j in alphabet:
#                 if i == j:
#                     go = False
#                     break
#                 else:
#                     x += 1
#         else:
#             break
#     while stop == False:
#         if alphabet[x] == chars[y]:
#             x += 1
#             y += 1
#         else:
#             return alphabet[x]
#             stop = True

# print find_missing_letter(['O','Q','R','S'])

chars = ['O','Q','R','S']
chars = "".join(chars)
chars = chars.lower()
chars = list(chars)
print chars