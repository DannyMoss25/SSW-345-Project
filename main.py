import convert
import solve
import FileFunctions as ff
import manualEnter as me

import tkinter as tk
from tkinter import messagebox as mb


fileFunction = ff.FileFunctions()



class main:
    def __init__(self):
        pass

    def File(self):

        def Edit():
            def EditFile():
                if(fileFunction.writeFileUI(inputtxt.get(1.0, "end-1c"), inputTxtTwo.get(1.0, "end-1c"))):
                    mb.showwarning(title="THE CHANGES WERE SAVED!", message="Changes were saved!")
                    o.destroy()
            n.destroy()
            o = tk.Tk()
            greetingFile = tk.Label(text="Name Of File to Edit")
            greetingFile.pack()
            inputtxt = tk.Text(o, height=2, width=20)
            inputtxt.pack()
            greetingFileTwo = tk.Label(text="New Formula")
            greetingFileTwo.pack()
            inputTxtTwo = tk.Text(o, height=2, width=20)
            inputTxtTwo.pack()
            buttonUse = tk.Button(o, text='Enter', width=25, command=EditFile)
            buttonUse.pack()

        def Use():
            def getFile():
                def EndOfUse():
                    for a in values:
                        values[a] = globals()['value%s' % a].get(1.0, "end-1c")
                    print(fileVal)
                    print(values)
                    print("CODE RUN")
                    mes = fileFunction.postProcessSolve(values, fileVal)
                    print(mes)
                    print("MES HERE")
                    mb.showwarning(title="Answer", message=mes)


                current = 0
                maxVal = 0
                fileVal = inputtxt.get(1.0, "end-1c")
                values = fileFunction.processFile(fileVal)
                o.destroy()
                p = tk.Tk()
                for x in values:
                    globals()['string%s' % x] = tk.Label(text="value of " + x)
                    globals()['string%s' % x].pack()
                    globals()['value%s' % x] = tk.Text(p, height=2, width=4)
                    globals()['value%s' % x].pack()
                buttonGetFile = tk.Button(p, text='Enter', width=25, command=EndOfUse)
                buttonGetFile.pack()




            n.destroy()
            o = tk.Tk()
            greetingFile = tk.Label(text="Name Of File")
            greetingFile.pack()
            inputtxt = tk.Text(o, height=2, width=20)
            inputtxt.pack()
            buttonUse = tk.Button(o, text='Enter', width=25, command=getFile)
            buttonUse.pack()




        print("File")
        m.destroy()
        n = tk.Tk()


        greetingFile = tk.Label(text="Edit Or Use?")
        greetingFile.pack()
        buttonFileOne = tk.Button(n, text='Edit', width=25, command=Edit)
        buttonFileOne.pack()
        buttonFileTwo = tk.Button(n, text='Use', width=25, command=Use)
        buttonFileTwo.pack()

    def Manual(self):
        def solve():
            manualEnter = me.manualEnter()
            mes = manualEnter.enterFormula((inputtxt.get(1.0, "end-1c")))
            mb.showwarning(title="Answer", message=mes)
        print("Manual")
        m.destroy()

        n = tk.Tk()
        greetingFile = tk.Label(text="Enter Formula")
        greetingFile.pack()
        inputtxt = tk.Text(n, height=2, width=20)
        inputtxt.pack()
        buttonUse = tk.Button(n, text='Enter', width=25, command=solve)
        buttonUse.pack()








m = tk.Tk()
'''
widgets are added here
'''
main = main()
greeting = tk.Label(text="hello! Work with File or Enter Values Manually?")
greeting.pack()
button = tk.Button(m, text='Work With File', width=25, command=main.File)
button.pack()


buttonTwo = tk.Button(m, text='Enter Values Manually', width=25, command=main.Manual)
buttonTwo.pack()


m.mainloop()




task = input("Do you want to write a formula or use a file? \n file: USE FILE \n Anything else is write a formula \n")




if(task == "file"):
    fileFunction.useFile()
else:
    manualEnter = me.manualEnter()
    manualEnter.inputForm()













