import tkinter
from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)
    print("BZZZZZZ")

window = Tk()
window.title("GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=30)

# label
my_label = Label(text="This is Label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"
my_label.config(text="New text")
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)



# Button
button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# New Button
new_button = Button(text="Click me new")
new_button.grid(column=2, row=0)



# Entry
input = Entry(width=20)
print(input.get())
# input.pack()
input.grid(column=3, row=2)




window.mainloop()
