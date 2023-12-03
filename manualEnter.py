import convert
import solve



def inputForm():
    value = input("Enter Formula")
    enterFormula(value)


def enterFormula(value):


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

    if(final[0][0] != "Error! "):
        print(final)
        print("Your answer is " + str(final[0][0]) + final[0][1])
    else:
        print(str(final[0][0]) + final[0][1])