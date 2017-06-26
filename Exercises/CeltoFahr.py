def tempConvert():
    while True:
        answer = raw_input("Are you trying to convert Celsius or Fahrenheit? ")
        answer = answer.lower()
        if answer == "celsius" or answer == "c":
            tempC = int(raw_input("Temperature in C? "))
            return C_to_F(tempC)
        elif answer == "fahrenheit" or answer == "f":
            tempF = int(raw_input("Temperature in F? "))
            return F_to_C(tempF)
        elif answer == "quit" or answer == "q":
            return "Goodbye"
        else:
            print "Please answer the question."

def C_to_F(temp):
    convC = ((( temp * 9) / 5) + 32)
    return "%.2f F" % convC

def F_to_C(temp):
    convF = ((( temp - 32) * 5) / 9)
    return "%.2f C" % convF


print tempConvert()