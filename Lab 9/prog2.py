from tkinter import Tk, Label, Entry, Button, messagebox


def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    result = num1 + num2
    print(result)
    result_entry.delete(0, "end")
    result_entry.insert(0, str(result))


window = Tk()
window.title("Hello world")
number1_label = Label(window, text="Number 1")
number1_label.grid(row=0, column=0)
number1_entry = Entry(window)
number1_entry.grid(row=0, column=1)
number2_label = Label(window, text="Number 2")
number2_label.grid(row=1, column=0)
number2_entry = Entry(window)
number2_entry.grid(row=1, column=1)
result_label = Label(window, text="Result")
result_label.grid(row=2, column=0)
result_entry = Entry(window)
result_entry.grid(row=2, column=1)
submit_button = Button(window, text="Submit", command=add)
submit_button.grid(row=3, column=0)
window.mainloop()
