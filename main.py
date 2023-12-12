import convert
import solve
import FileFunctions
import manualEnter

import tkinter as tk
from tkinter import messagebox as mb






class main:
    def __init__(self):
        pass

    @staticmethod
    def File():

        def Edit():
            def EditFile():
                if(FileFunctions.FileFunctions.writeFileUI(inputtxt.get(1.0, "end-1c"), inputTxtTwo.get(1.0, "end-1c"))):
                    mb.showwarning(title="THE CHANGES WERE SAVED!", message="Changes were saved!")
                    o.destroy()
            n.destroy()
            o = tk.Tk()
            greetingFile = tk.Label(text="Name Of File to Edit", font=('Times New Roman', 15, 'bold'))
            greetingFile.pack()
            inputtxt = tk.Text(o, height=2, width=20, font=('Times New Roman', 15, 'bold'))
            inputtxt.pack()
            greetingFileTwo = tk.Label(text="New Formula", font=('Times New Roman', 15, 'bold'))
            greetingFileTwo.pack()
            inputTxtTwo = tk.Text(o, height=2, width=20, font=('Times New Roman', 15, 'bold'))
            inputTxtTwo.pack()
            buttonUse = tk.Button(o, text='Enter', width=25, command=EditFile, height=5, font=('Times New Roman', 15, 'bold'))
            buttonUse.pack()

        def Use():
            def getFile():
                def EndOfUse():
                    for a in values:
                        values[a] = globals()['value%s' % a].get(1.0, "end-1c")
                    print(fileVal)
                    print(values)
                    print("CODE RUN")
                    mes = FileFunctions.FileFunctions.postProcessSolve(values, fileVal)
                    print(mes)
                    print("MES HERE")
                    mb.showwarning(title="Answer", message=mes)


                current = 0
                maxVal = 0
                fileVal = inputtxt.get(1.0, "end-1c")
                values = FileFunctions.FileFunctions.processFile(fileVal)
                o.destroy()
                p = tk.Tk()
                for x in values:
                    globals()['string%s' % x] = tk.Label(text="value of " + x, font=('Times New Roman', 15, 'bold'))
                    globals()['string%s' % x].pack()
                    globals()['value%s' % x] = tk.Text(p, height=2, width=25, font=('Times New Roman', 15, 'bold'))
                    globals()['value%s' % x].pack()
                buttonGetFile = tk.Button(p, text='Enter', width=25, command=EndOfUse, height=5, font=('Times New Roman', 15, 'bold'))
                buttonGetFile.pack()




            n.destroy()
            o = tk.Tk()
            greetingFile = tk.Label(text="Name Of File", font=('Times New Roman', 15, 'bold'))
            greetingFile.pack()
            inputtxt = tk.Text(o, height=2, width=20, font=('Times New Roman', 15, 'bold'))
            inputtxt.pack()
            buttonUse = tk.Button(o, text='Enter', width=25, command=getFile, height=5, font=('Times New Roman', 15, 'bold'))
            buttonUse.pack()




        print("File")
        m.destroy()
        n = tk.Tk()


        greetingFile = tk.Label(text="Edit Or Use?", font=('Times New Roman', 15, 'bold'))
        greetingFile.pack()
        buttonFileOne = tk.Button(n, text='Edit', width=25, command=Edit, height=5, font=('Times New Roman', 15, 'bold'))
        buttonFileOne.pack()
        buttonFileTwo = tk.Button(n, text='Use', width=25, command=Use, height=5, font=('Times New Roman', 15, 'bold'))
        buttonFileTwo.pack()

    @staticmethod
    def Manual():
        def solve():
            mes = manualEnter.manualEnter.enterFormula((inputtxt.get(1.0, "end-1c")))
            mb.showwarning(title="Answer", message=mes)
        print("Manual")
        m.destroy()

        n = tk.Tk()
        greetingFile = tk.Label(text="Enter Formula", font=('Times New Roman', 15, 'bold'))
        greetingFile.pack()
        inputtxt = tk.Text(n, height=2, width=50,font=('Times New Roman', 15, 'bold'))
        inputtxt.pack()
        buttonUse = tk.Button(n, text='Enter', width=25, command=solve, height=5, font=('Times New Roman', 15, 'bold'))
        buttonUse.pack()








m = tk.Tk()

'''
widgets are added here
'''
main = main()
greeting = tk.Label(text="Work with File or Enter Formula Manually?",font=('Times New Roman', 15, 'bold'))
greeting.pack()
button = tk.Button(m, text='Work With File', width=20, command=main.File, height=5, font=('Times New Roman', 15, 'bold'))
button.pack()


buttonTwo = tk.Button(m, text='Enter Values Manually', width=20, command=main.Manual, height=5, font=('Times New Roman', 15, 'bold'))
buttonTwo.pack()


m.mainloop()























