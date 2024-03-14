from tkinter import *
from tkinter import messagebox

window = Tk()
label = Label(window, text="Enter your name:")
label.grid(row=0, column=0)
entry = Entry(window, width=10)
entry.grid(row=0, column=1)

def submit():
    name = entry.get()
    messagebox.showinfo("Name", "Hello, " + name)

button = Button(window, text="Submit", command=submit)
button.grid(row=1, column=0, columnspan=2)

window.mainloop()
