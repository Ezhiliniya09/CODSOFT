# Python program to create a Calculator  
 
# import Tkinter module 
from tkinter import *
 
# Global declaration of Expression variable 
expression = "" 
 
 
# Function to update expression  
def press(num):  
    global expression  
    expression = expression + str(num) 
    equation.set(expression) 
 
# Function to evaluate the final expression 
def equalpress():  
    try: 
        global expression  
        total = str(eval(expression)) 
        equation.set(total) 
        expression = "" 
    except: 
        equation.set(" error ") 
        expression = "" 
 
# Function to clear the contents  
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
 
# Driver code 
if __name__ == "__main__": 
    # Create a GUI window 
    gui = Tk() 
 
    # Background colour 
    gui.configure(background="black") 
 
    # Title 
    gui.title("Simple Calculator") 
 
    # Layout 
    gui.geometry("270x310")
    equation = StringVar()

    # Text entry box
    expression_field = Entry(gui, textvariable=equation, bg='gray23', fg='white') 
    expression_field.grid(columnspan=4, ipadx=73 , ipady=5)
 
    # Create a Buttons and place at a particular 
    button1 = Button(gui, text=' 1 ', fg='white', bg='gray26', 
                    command=lambda: press(1), height=3, width=7) 
    button1.grid(row=5, column=0) 
 
    button2 = Button(gui, text=' 2 ', fg='white', bg='gray26', 
                    command=lambda: press(2), height=3, width=7) 
    button2.grid(row=5, column=1) 
 
    button3 = Button(gui, text=' 3 ', fg='white', bg='gray26', 
                    command=lambda: press(3), height=3, width=7) 
    button3.grid(row=5, column=2) 
 
    button4 = Button(gui, text=' 4 ', fg='white', bg='gray26', 
                    command=lambda: press(4), height=3, width=7) 
    button4.grid(row=4, column=0) 
 
    button5 = Button(gui, text=' 5 ', fg='white', bg='gray26', 
                    command=lambda: press(5), height=3, width=7) 
    button5.grid(row=4, column=1) 
 
    button6 = Button(gui, text=' 6 ', fg='white', bg='gray26', 
                    command=lambda: press(6), height=3, width=7) 
    button6.grid(row=4, column=2) 
 
    button7 = Button(gui, text=' 7 ', fg='white', bg='gray26', 
                    command=lambda: press(7), height=3, width=7) 
    button7.grid(row=3, column=0) 
 
    button8 = Button(gui, text=' 8 ', fg='white', bg='gray26', 
                    command=lambda: press(8), height=3, width=7) 
    button8.grid(row=3, column=1) 
 
    button9 = Button(gui, text=' 9 ', fg='white', bg='gray26', 
                    command=lambda: press(9), height=3, width=7) 
    button9.grid(row=3, column=2) 
 
    button0 = Button(gui, text=' 0 ', fg='white', bg='gray26', 
                    command=lambda: press(0), height=3, width=7) 
    button0.grid(row=6, column=0) 
 
    plus = Button(gui, text=' + ', fg='white', bg='gray', 
                command=lambda: press("+"), height=3, width=7) 
    plus.grid(row=3, column=3) 
 
    minus = Button(gui, text=' - ', fg='white', bg='gray', 
                command=lambda: press("-"), height=3, width=7) 
    minus.grid(row=4, column=3) 
 
    multiply = Button(gui, text=' * ', fg='white', bg='gray', 
                    command=lambda: press("*"), height=3, width=7) 
    multiply.grid(row=5, column=3) 
 
    divide = Button(gui, text=' / ', fg='white', bg='gray', 
                    command=lambda: press("/"), height=3, width=7) 
    divide.grid(row=6, column=3) 
 
    equal = Button(gui, text=' = ', fg='white', bg='gray', 
                command=equalpress, height=3, width=7) 
    equal.grid(row=6, column=2) 
 
    clear = Button(gui, text='Clear', fg='white', bg='PaleVioletRed3', 
                command=clear, height=3, width=7) 
    clear.grid(row=2, column=0) 
 
    Decimal= Button(gui, text='.', fg='white', bg='gray', 
                    command=lambda: press('.'), height=3, width=7) 
    Decimal.grid(row=6, column=1) 
    # start the GUI 
    gui.mainloop() 
