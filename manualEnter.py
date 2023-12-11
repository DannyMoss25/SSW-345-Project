import convert as con
import solve as sol

convert = con.convert()
solve = sol.solve()


class manualEnter:
    def __init__(self):
        pass

    def inputForm(self):
        value = input("Enter Formula")
        manualEnter.enterFormula(value)


    def enterFormula(self, value):


        valueSplitted = [""]

        currentValue = 0



        value = value.replace(" ", "")



        for i in value:
            if (i == "+" or i == "/" or i == "*" or i == "-"):
                if(i == "-"):
                    if(valueSplitted[currentValue - 1] == "0" or valueSplitted[currentValue - 1] == "1" or valueSplitted[currentValue - 1] == "2" or valueSplitted[currentValue - 1] == "3" or valueSplitted[currentValue - 1] == "4" or valueSplitted[currentValue - 1] == "5" or valueSplitted[currentValue - 1] == "6" or valueSplitted[currentValue - 1] == "7" or valueSplitted[currentValue - 1] == "8" or valueSplitted[currentValue - 1] == "9"):
                        valueSplitted.append(i)
                        valueSplitted.append("")
                        currentValue += 2
                    else:
                        valueSplitted[currentValue] = valueSplitted[currentValue] + i
                else:
                    valueSplitted.append(i)
                    valueSplitted.append("")
                    currentValue += 2
            else:
                valueSplitted[currentValue] = valueSplitted[currentValue] + i

        converted = convert.convert(valueSplitted)
        print("Here is what was")
        print(converted)

        final = solve.calc(converted)
        print("THIS WAS WAS SET OFF")
        print(final)
        if(final[0][0] != "Error! "):
            return "Your answer is " + str(final[0][0]) + final[0][1]
            #print("Your answer is " + str(final[0][0]) + final[0][1])
        else:
            return (str(final[0][0]) + final[0][1])
            #print(str(final[0][0]) + final[0][1])