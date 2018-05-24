#       __                 _   _____ _   _                 
#      /__\ ___  ___ _   _| | /__   (_) (_)_______ _ __    
#     / \/// _ \/ __| | | | |   / /\/ | | |_  / _ \ '_ \   
#    / _  \  __/\__ \ |_| | |  / /  | |_| |/ /  __/ | | |  
#    \/ \_/\___||___/\__,_|_|  \/    \__,_/___\___|_| |_|  
#

# This program is for Python and Tkinter GUI 3X version.
# Creation Time: 22.05.2018 - 06:15 / Resul TÜZEN

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Calculator")
window.geometry("250x140")
window.resizable(width = False, height = False)

def clean():
    FirstNumber.delete(0, END)
    SecondNumber.delete(0, END)
    
def addition():
    addition = int(FirstNumber.get()) + int(SecondNumber.get())
    messagebox.showinfo("Addition", addition)
    clean()
    
def division():
    division = int(FirstNumber.get()) / int(SecondNumber.get())
    messagebox.showinfo("Division", division)
    clean()

def extraction():
    extraction = int(FirstNumber.get()) - int(SecondNumber.get())
    messagebox.showinfo("Extraction", extraction)
    clean()

def multiplication():
    multiplication = int(FirstNumber.get()) * int(SecondNumber.get())
    messagebox.showinfo("Multiplication", multiplication)
    clean()


L1 = Label(text = "First Number:")
L1.place(x = 25, y = 6)

FirstNumber = Entry(text = "")
FirstNumber.place(x = 110, y = 8)

L1 = Label(text = "Second Number:")
L1.place(x = 10, y = 42)

SecondNumber = Entry(text = "")
SecondNumber.place(x = 110, y = 45)

addButon = Button(text = "Addition", bg="orange", width = "9", command = addition)
addButon.place(x = 87, y = 105)

divisionButon = Button(text = "Division", bg="deep sky blue", width = "9", command = division)
divisionButon.place(x = 165, y = 105)

extractionButon = Button(text = "Extraction", bg="green", width = "9", command = extraction)
extractionButon.place(x = 10, y = 105)

multiplicationButon =  Button(text = "Multiplication", bg="gray65", width = "31", command = multiplication)
multiplicationButon.place(x = 10, y = 75)

mainloop()
