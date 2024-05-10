import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Hello, Tkinter",foreground="white",background="black")
label.pack()

labelName = tk.Label(text="Name")
entry = tk.Entry()

labelName.pack()
entry.pack();

name = entry.get()
print(name)
window.mainloop()
