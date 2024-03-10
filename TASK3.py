# Import modules
from tkinter import *   
import random

# Create a GUI window
root = Tk()

# Background colour 
root.configure(background="#0000FF") 
 
# Title 
root.title("Strong Password Generator")

# Layout
root.geometry("500x250")

userid = StringVar()
passwrd = StringVar()
passlen = IntVar()
 
# Function to generate password
def generate(): 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)
  
# Labels
Label(root,
      text="Strong Password Generator",
      font="Impact 30 bold",
      bg = "#0000FF",
      fg="#FFFFFF"
      ).pack()

Label(root,
      text="Enter Username",
      bg = "#0000FF",
      fg="#FFFFFF",
      font="Impact"
      ).pack(pady=3)

Entry(root,
      textvariable=userid,
      width = 35
      ).pack(pady=3)

Label(root,
      text="Enter the number to get password",
      bg = "#0000FF",
      fg="#FFFFFF",
      font="Impact"
      ).pack(pady=3)

Entry(root,
      textvariable=passlen,
      width = 35
      ).pack(pady=3)

Button(root,
       text="Generate",
       command=generate,
       bg = "#FACC52",
       width = 25,
       fg="#000000",
       font="Impact"
       ).pack(pady=7)

Entry(root,
      textvariable=passwrd,
      width = 35
      ).pack(pady=3)

# start the GUI 
root.mainloop()
