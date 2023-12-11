
class conversionRates:
    def __init__(self):
        pass

    def rates(self, values):
        splitted = []
        powers = []
        current = ""

        tot = len(values)
        it = 0
        while (tot > it):
            i = values[it]

            if(i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "-"):
                splitted.append(current)
                current = ""
                power = ""
                j = values[it]
                keepGoing = True
                while (keepGoing):
                    if(j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9" or j == "-"):
                        power += str(j)
                        it += 1
                        if not(it > len(values) - 1):
                            j = values[it]
                        else:
                            keepGoing = False
                            powers.append(power)
                            it -= 1
                    else:
                        it -= 1
                        keepGoing = False
                        powers.append(power)
            else:
                current += i
            it += 1
        if(current != ""):
            splitted.append(current)
            powers.append("1")


        changeOfNumber = 1
        changeOfUnits = []




        for b in range(len(powers)):
            powers[b - 1] = powers[b - 1].replace('\U00002013', '-')

        for b in range(len(splitted)):
            a=splitted[b]
            if(a == "hr"):
                changeOfNumber *= 60**float(powers[b])
                changeOfUnits.append("s" + str(powers[b]))
            if (a == "s"):
                changeOfNumber *= 1 ** float(powers[b])
                changeOfUnits.append("s" + str(powers[b]))
            elif(a == "mm"):
                changeOfNumber *= .001**float(powers[b])
                changeOfUnits.append("m" + str(powers[b]))
            elif(a == "in"):
                changeOfNumber *= 0.0254 ** float(powers[b])
                changeOfUnits.append("m" + str(powers[b]))
            elif (a == "miles"):
                changeOfNumber *= 1609.34 ** float(powers[b])
                changeOfUnits.append("m" + str(powers[b]))
            elif(a == "km"):
                changeOfNumber *= 1000**float(powers[b])
                changeOfUnits.append("m" + str(powers[b]))
            elif (a == "cm"):
                changeOfNumber *= .01**float(powers[b])
                changeOfUnits.append("m" + str(powers[b]))
            elif (a == "m"):
                changeOfNumber *= 1**float(powers[b])
                changeOfUnits.append("m" + str(powers[b]))
            elif (a == "mg"):
                changeOfNumber *= .001 **float(powers[b])
                changeOfUnits.append("g" + str(powers[b]))
            elif (a == "kg"):
                changeOfNumber *= 1000 **float(powers[b])
                changeOfUnits.append("g" + str(powers[b]))
            elif (a == "cg"):
                changeOfNumber *= .01 **float(powers[b])
                changeOfUnits.append("g" + str(powers[b]))
            elif (a == "g"):
                changeOfNumber *= 1 **float(powers[b])
                changeOfUnits.append("g" + str(powers[b]))
            else:
                pass

        changeOfUnits.sort()
        changeOfUnitsFinal = ''.join(changeOfUnits)


        return[changeOfNumber, changeOfUnitsFinal]










