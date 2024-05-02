from tkinter import *

window = Tk()
window.geometry("300x300")
header = Label(window, text="Hello!", justify="center")
header.grid(column=1, row=0, columnspan=2)
label = Label(window, text="Hello, world!")
button = Button(window, text="Click me!", command=lambda:print("Clicked"))
label.grid(row=0, column=0)
button.grid(row=1, column=1)
window.mainloop()