from tkinter import *
from tkinter import messagebox

window = Tk()

name_var = StringVar()
name_entry = Entry(window, textvariable=name_var)
def submit():
   name = name_var.get()
   messagebox.showinfo(title = "Hello!", message=f'Hello {name}')
submit_button = Button(window, command=submit, text="Submit")
name_entry.pack()
submit_button.pack()
window.mainloop()