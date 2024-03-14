from tkinter import *
from tkinter import messagebox

window = Tk()
menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=lambda: messagebox.showinfo("New File", "New File Created"))
file_menu.add_command(label="New Project", command=lambda: messagebox.showinfo("New Project", "New Project Created"))
file_menu.add_separator()
file_menu.add_command(label="Quit", command=window.quit)
edit_menu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_separator()
edit_menu.add_command(label="Paste")
window.mainloop()