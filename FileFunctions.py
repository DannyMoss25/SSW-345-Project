import manualEnter as me



def writeFile():
    fileName = input("Enter name of file you wish to edit")
    newName = input("Enter the new contents of the file")
    file1 = open(fileName, 'w')
    file1.write(newName)
    file1.close()
    pass

def solveFile():
    fileName = input("Enter name of file")
    fRaw = open(fileName, "r")
    f = fRaw.read()
    specialChar = {}
    for a in range(len(f)):
        if (f[a] != "*" and f[a] != "/" and f[a] != "-" and f[a] != "+" and f[a] != " " and f[a].isdigit() == False):
            specialChar[f[a]] = "io"

    for a in specialChar:
        specialChar[a] = input("What is the value of " + a + "?")

    finalSolve = ""
    for a in f:
        if (a != "*" and a != "/" and a != "-" and a != "+" and a != " " and a.isdigit() == False):
            finalSolve += specialChar[a]
        else:
            finalSolve += a
    me.enterFormula(finalSolve)




def useFile():
    fileName = input("Do you want to edit a file or use a file?\n edit: edit the file \n use: use file\n")
    if(fileName == "edit"):
        writeFile()
    else:
        solveFile()













