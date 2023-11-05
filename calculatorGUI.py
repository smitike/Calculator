# create a GUI calculator using tkinter
# date: Mar 6, 2023
# author: Selam Mitike
# file: calculatorGUI.py a Python program that creates a calculator in a gui window and entrybox for solutions
# input: expressions to be calculated
# output: solution of the expression as a decimal
from tkinter import *
from tkinter import ttk
from calculator import calculate

def calculator(gui):
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=
    b0 = addButton(gui, entrybox, '0')
    b1 = addButton(gui, entrybox, '1')
    b2 = addButton(gui, entrybox, '2')
    b3 = addButton(gui, entrybox, '3')
    b4 = addButton(gui, entrybox, '4')
    b5 = addButton(gui, entrybox, '5')
    b6 = addButton(gui, entrybox, '6')
    b7 = addButton(gui, entrybox, '7')
    b8 = addButton(gui, entrybox, '8')
    b9 = addButton(gui, entrybox, '9')
    b_add = addButton(gui, entrybox, '+')
    b_sub = addButton(gui, entrybox, '-')
    b_mult = addButton(gui, entrybox, '*')
    b_div = addButton(gui, entrybox, '/')
    b_clr = addButton(gui, entrybox, 'c')
    b_eq = addButton(gui, entrybox, '=')

    # add buttons to the grid
    buttons = [b7, b8, b9, b_clr,
               b4, b5, b6, b_sub,
               b1, b2, b3, b_add,
               b_mult, b0, b_div, b_eq]
    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i * k + j].grid(row=i + 1, column=j, columnspan=1)


def addButton(gui, entrybox, value):
    entrybox.delete(0, END)
    return Button(gui, text=value, height=4, width=9, command=lambda: clickButton(entrybox, value))


def clickButton(entrybox, value):
    # the function clickButton() is not implemented!!!
    username = StringVar()
    input = ttk.Entry(gui, textvariable=username)
    entrybox.insert(len(entrybox.get()), value) # displays the values in the entrybox
    if value == '=': # if = sign is clicked, it calls the function calculate with the expression
        entrybox.delete(first=len(entrybox.get())-1, last="end")
        expression = entrybox.get()
        answer = calculate(expression) # calculates the expression from the exntrybox and returns the answer
        entrybox.delete(0, END) # deletes the expression
        entrybox.insert(0, answer) # displays the answer
    if value =='c': # c clears the entry box
        entrybox.delete(0, END)

    #equation.set(expression)

    print(value)  # for debugging


# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()
