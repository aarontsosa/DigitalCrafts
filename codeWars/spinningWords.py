

sentence = list("to")
length = len(sentence)
sentence.insert(length, " ")
wordCounter = 0
counter = 0
new = [ ]
holder = 0
while counter <= length:
    if sentence[counter] == " ":
        if wordCounter >= 5:
            wordCounter = wordCounter - 1
            holder = counter - 1
            while wordCounter >= 0:
                new.insert(counter, sentence[holder])
                wordCounter = wordCounter - 1
                holder = holder - 1
            counter = counter + 1
            wordCounter = 0
            new.insert(counter, " ")
        else:
            holder = counter - wordCounter
            wordCounter = wordCounter - 1
            while holder <= counter:
                new.insert(counter, sentence[holder])
                holder = holder + 1
            holder = 0
            wordCounter = 0
            counter = counter + 1
    else:
        counter = counter + 1
        wordCounter = wordCounter + 1
new.pop()
print "".join(new)