import math


def newUnitsDiv(one, two):
    print(one)
    gramsOne = ""
    gramsTwo = ""
    metersOne = ""
    metersTwo = ""
    secondsOne = ""
    secondsTwo = ""
    num = len(one)
    a = 0
    while (a < num):


        if(one[a] == "g"):
            b = a + 1
            keepGoing = True
            while (b < len(one) and keepGoing == True):
                current = one[b]
                if(current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    gramsOne += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (one[a] == "m"):
            b = a + 1
            keepGoing = True
            while (b < len(one) and keepGoing == True):
                current = one[b]
                if (current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    metersOne += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (one[a] == "s"):
            print("Set off")
            b = a + 1
            keepGoing = True
            while (b < len(one) and keepGoing == True):
                current = one[b]
                if (current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    secondsOne += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        a += 1
        print(a)


    num = len(two)
    a = 0
    while (a < num):

        if(two[a] == "g"):
            b = a + 1
            keepGoing = True
            while (b < len(two) and keepGoing == True):

                current = two[b]
                if(current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    gramsTwo += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (two[a] == "m"):
            b = a + 1
            keepGoing = True
            while (b < len(two) and keepGoing == True):
                current = two[b]
                if (
                        current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    metersTwo += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (two[a] == "s"):
            b = a + 1
            keepGoing = True
            while (b < len(two) and keepGoing == True):
                current = two[b]
                if (
                        current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    secondsTwo += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        a += 1


    finalreturn = ""

    if(gramsOne != "" or gramsTwo!=""):
        if(gramsOne == ""):
            value = float(gramsTwo) * -1
        elif(gramsTwo == ""):
            value = float(gramsOne)
        else:
            value = float(gramsOne) - float(gramsTwo)
        finalreturn +=  "g" + str(math.floor(value))

    if (metersOne != "" or metersTwo != ""):
        if (metersOne == ""):
            value = float(metersTwo) * -1
        elif (metersTwo == ""):
            value = float(metersOne)
        else:
            value = float(metersOne) - float(metersTwo)
        finalreturn += "m" + str(math.floor(value))

    if (secondsOne != "" or secondsTwo != ""):
        if (secondsOne == ""):
            value = float(secondsTwo) * -1
        elif (secondsTwo == ""):
            value = float(secondsOne)
        else:
            value = float(secondsOne) - float(secondsTwo)
        finalreturn += "s" + str(math.floor(value))
    print("OUT COME")
    print(finalreturn)
    return finalreturn

    print("EndedTwo")







def newUnitsMult(one, two):
    print(one)
    gramsOne = ""
    gramsTwo = ""
    metersOne = ""
    metersTwo = ""
    secondsOne = ""
    secondsTwo = ""
    num = len(one)
    a = 0
    while (a < num):


        if(one[a] == "g"):
            b = a + 1
            keepGoing = True
            while (b < len(one) and keepGoing == True):
                current = one[b]
                if(current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    gramsOne += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (one[a] == "m"):
            b = a + 1
            keepGoing = True
            while (b < len(one) and keepGoing == True):
                current = one[b]
                if (current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    metersOne += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (one[a] == "s"):
            print("Set off")
            b = a + 1
            keepGoing = True
            while (b < len(one) and keepGoing == True):
                current = one[b]
                if (current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    secondsOne += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        a += 1
        print(a)


    num = len(two)
    a = 0
    while (a < num):

        if(two[a] == "g"):
            b = a + 1
            keepGoing = True
            while (b < len(two) and keepGoing == True):

                current = two[b]
                if(current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    gramsTwo += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (two[a] == "m"):
            b = a + 1
            keepGoing = True
            while (b < len(two) and keepGoing == True):
                current = two[b]
                if (
                        current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    metersTwo += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        if (two[a] == "s"):
            b = a + 1
            keepGoing = True
            while (b < len(two) and keepGoing == True):
                current = two[b]
                if (
                        current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9" or current == "-"):
                    secondsTwo += str(current)
                    a = b
                    b += 1
                else:
                    keepGoing = False
        a += 1


    finalreturn = ""

    if(gramsOne != "" or gramsTwo!=""):
        if(gramsOne == ""):
            value = float(gramsTwo)
        elif(gramsTwo == ""):
            value = float(gramsOne)
        else:
            value = float(gramsOne) + float(gramsTwo)
        finalreturn +=  "g" + str(math.floor(value))

    if (metersOne != "" or metersTwo != ""):
        if (metersOne == ""):
            value = float(metersTwo)
        elif (metersTwo == ""):
            value = float(metersOne)
        else:
            value = float(metersOne) + float(metersTwo)
        finalreturn += "m" + str(math.floor(value))

    if (secondsOne != "" or secondsTwo != ""):
        if (secondsOne == ""):
            value = float(secondsTwo)
        elif (secondsTwo == ""):
            value = float(secondsOne)
        else:
            value = float(secondsOne) + float(secondsTwo)
        finalreturn += "s" + str(math.floor(value))
    print("OUT COME")
    print(finalreturn)
    return finalreturn

    print("EndedTwo")

#Testing Again
#Testing to update the git
#test
























