from tkinter import *

window = Tk()
entry = Entry(window, width=10)
entry.pack()
def submit():
    name = entry.get()
    print(name)
button = Button(window, text="Submit", command=submit)
button.pack()
window.mainloop()