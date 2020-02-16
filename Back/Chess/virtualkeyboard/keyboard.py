from tkinter import *
import tkinter as tkinter

k_app = tkinter.Tk()
k_app.title('keyboard')
k_app.config(background='black')
k_app.wm_iconbitmap()
k_app.resizable(0, 0)
appname = Label(k_app, text='Onscreen Keyboard',
                font=('arial', 20, 'bold'), background='black', foreground='white').grid(row=0, columnspan=40)
var_row = 4
var_column = 0
box = Text(k_app, width=90, height=15, font=('arial', 15, 'bold'))
box.grid(row=1, columnspan=40)

buttons = ['~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'z', 'e', 'r', 't',
           'y', 'u', 'i', 'o', 'p', 'q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w',
           'x', 'c', 'v', 'b', 'n', '=', '_', '-', ',', ';', '.', ':', '/', '!', '*', '[',
           ']', 'Back space', 'Enter', 'Tab'
    , 'Space']


def select(x):
    if x == 'Space':
        box.insert(tkinter.END, ' ')
    elif x == 'Enter':
        box.insert(INSERT, '\n')
    elif x == 'Tab':
        box.insert(tkinter.END, '    ')
    elif x == 'Back space':
        box.delete(1.0)
    # elif x == 'Maj':
    #     box.insert(tkinter.END,''.upper())
    else:
        box.insert(tkinter.END, x)


for button in buttons:
    command = lambda x=button: select(x)

    if button == 'Space':
        tkinter.Button(k_app, text=button, width=10, padx=3, pady=3, bd=12, background='black', relief='raised',
                       foreground='white',
                       command=command).grid(row=var_row, column=var_column)
    else:
        button = tkinter.Button(k_app, text=button, width=8, padx=3, pady=3, bd=10, background='black', relief='raised',
                                foreground='white',
                                command=command).grid(row=var_row, column=var_column)
        var_column += 1
    if var_column > 15 and var_row == 2:
        var_column = 0
        var_row += 1
    if var_column > 15 and var_row == 3:
        var_column = 0
        var_row += 1
    if var_column > 15 and var_row == 4:
        var_column = 0
        var_row += 1
    if var_column > 15 and var_row == 5:
        var_column = 0
        var_row += 1
    if var_column > 15 and var_row == 6:
        var_column = 0
        var_row += 1

k_app.mainloop()
