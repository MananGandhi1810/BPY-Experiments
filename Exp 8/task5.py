from tkinter import *

window = Tk()
window.title("Select a bank")
window.geometry("300x300")
var = StringVar()
r1 = Radiobutton(window, text="SBI", value="SBI", variable=var)
r1.pack()
r2 = Radiobutton(window, text="ICICI", value="ICICI", variable=var)
r2.pack()
r3 = Radiobutton(window, text="HDFC", value="HDFC", variable=var)
r3.pack()
r4 = Radiobutton(window, text="Axis", value="Axis", variable=var)
r4.pack()
r5 = Radiobutton(window, text="Kotak", value="Kotak", variable=var)
r5.pack()
button = Button(window, text="Submit", command=lambda: print(var.get()))
button.pack()
window.mainloop()