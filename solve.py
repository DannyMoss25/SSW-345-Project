import newUnits as nu

newUnits = nu.newUnits



class solve:
    def __init__(self):
        pass
    from tkinter import messagebox as mb
    def calc(self, prompt):

        add = []
        subtract = []
        multiply = []
        divide = []
        loc = 0
        for i in prompt:
            if(i[1] == "+"):
                add.append(loc)
            elif(i[1] == "-"):
                subtract.append(loc)
            elif(i[1] == "*"):
                multiply.append(loc)
            elif(i[1] == "/"):
                divide.append(loc)
            loc += 1


        for i in multiply:
            print('issue here')
            print(prompt)
            prompt[i - 1][0] = float(prompt[i - 1][0]) * float(prompt[i + 1][0])


            prompt[i - 1][1] = newUnits.newUnitsMult(newUnits, prompt[i - 1][1], prompt[i + 1][1])


            prompt.pop(i)
            prompt.pop(i)

            fix = 0
            for j in multiply:
                if j > i:
                    multiply[fix] = multiply[fix] - 2
                fix += 1
            fix = 0
            for j in subtract:
                if j > i:
                    subtract[fix] = subtract[fix] - 2
                fix += 1
            fix = 0
            for j in add:
                if j > i:
                    add[fix] = add[fix] - 2
                fix += 1
            fix = 0
            for j in divide:
                if j > i:
                    divide[fix] = divide[fix] - 2
                fix += 1


        for i in divide:
            prompt[i - 1][0] = float(prompt[i - 1][0]) / float(prompt[i + 1][0])


            prompt[i - 1][1] = newUnits.newUnitsDiv(newUnits, prompt[i - 1][1], prompt[i + 1][1])


            firstRemoved = prompt[i]
            secondRemoved = prompt[i + 1]

            prompt.pop(i)
            prompt.pop(i)

            fix = 0
            for j in multiply:
                if j > i:
                    multiply[fix] = multiply[fix] - 2
                fix += 1
            fix = 0
            for j in subtract:
                if j > i:
                    subtract[fix] = subtract[fix] - 2
                fix += 1
            fix = 0
            for j in add:
                if j > i:
                    add[fix] = add[fix] - 2
                fix += 1
            fix = 0
            for j in divide:
                if j > i:
                    divide[fix] = divide[fix] - 2
                fix += 1

        for i in add:
            if not(str(prompt[i - 1][1]) == str(prompt[i + 1][1])):
                print(prompt)
                print("ONE VLA")
                print(str(prompt[i - 1][1]))
                print("TWO VLA")
                print(str(prompt[i + 1][1]))
                return[["Error! ", "You are trying to add two different types of units! YOU CANNOT DO THAT!"]]

            prompt[i - 1][0] = float(prompt[i - 1][0]) + float(prompt[i + 1][0])
            prompt[i - 1][1] = prompt[i - 1][1]

            firstRemoved = prompt[i]
            secondRemoved = prompt[i + 1]

            prompt.pop(i)
            prompt.pop(i)

            fix = 0
            for j in multiply:
                if j > i:
                    multiply[fix] = multiply[fix] - 2
                fix += 1
            fix = 0
            for j in subtract:
                if j > i:
                    subtract[fix] = subtract[fix] - 2
                fix += 1
            fix = 0
            for j in add:
                if j > i:
                    add[fix] = add[fix] - 2
                fix += 1
            fix = 0
            for j in divide:
                if j > i:
                    divide[fix] = divide[fix] - 2
                fix += 1

        for i in subtract:
            if not(str(prompt[i - 1][1]) == str(prompt[i + 1][1])):
                return[["Error! ", "You are trying to add two different types of units! YOU CANNOT DO THAT!"]]

            prompt[i - 1][0] = float(prompt[i - 1][0]) - float(prompt[i + 1][0])
            prompt[i - 1][1] = prompt[i - 1][1]

            firstRemoved = prompt[i]
            secondRemoved = prompt[i + 1]

            prompt.pop(i)
            prompt.pop(i)
            for j in multiply:
                if j > i:
                    multiply[fix] = multiply[fix] - 2
                fix += 1
            fix = 0
            for j in subtract:
                if j > i:
                    subtract[fix] = subtract[fix] - 2
                fix += 1
            fix = 0
            for j in add:
                if j > i:
                    add[fix] = add[fix] - 2
                fix += 1
            fix = 0
            for j in divide:
                if j > i:
                    divide[fix] = divide[fix] - 2
                fix += 1
        return prompt









