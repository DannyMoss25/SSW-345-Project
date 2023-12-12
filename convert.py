import conversionRates


class convert:
    def __init__(self):
        pass

    @staticmethod
    def convert(values):
        result = []
        saved = ""
        for i in values:
            if not(i == "+" or i == "/" or i == "*" or i == "-"):
                unit = ""
                moment = 0
                value = len(i)
                stopped = False
                while (value > 0):
                    current = i[value - 1]
                    if (current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9"):
                        pass
                    else:
                        unit = ""
                        for a in reversed(range(len(i) - (value - 1))):
                            unit = unit + i[len(i) - a - 1]
                        moment = value - 1
                    value = value - 1

                unitless = True
                for current in i:
                    if not(current == "0" or current == "1" or current == "2" or current == "3" or current == "4" or current == "5" or current == "6" or current == "7" or current == "8" or current == "9"):
                        unitless = False
                if(unitless == True):
                    result.append([i, ""])
                else:
                    result.append([i[0: moment], unit])
            else:
                result.append(["|", i])

        for value in result:
            if(value[0] != "|"):
                conversionValues = conversionRates.conversionRates.rates(value[1])
                value[0] = float(value[0]) * float(conversionValues[0])
                value[1] = conversionValues[1]
        return result









