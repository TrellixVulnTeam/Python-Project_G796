from tkinter import *

root = Tk()

def printName(event):
    print("i am Bikash")

button_1 = Button(root, text="Print Name")
button_1.bind("<Button-1>", printName)
button_1.pack()

root.mainloop()