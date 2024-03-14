from tkinter import *
import sys

window = Tk()
text = Text(window, width=40, height=10)
text.pack()
text.insert(INSERT, "print(\"Hello, World!\")\n")

def submit():
    code = text.get("1.0", END)
    try:
        exec(code)
    except Exception as e:
        text.insert(END, f"\nError: {e}")

submit_button = Button(window, text="Run", command=submit)
submit_button.pack()

window.mainloop()