from tkinter import *


def action():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f"{km}")


window = Tk()

window.title("Mile to Km Converter")
# window.minsize(width=60, height=40)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(END, "0")
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=action)
calculate_button.grid(row=2, column=1)

mainloop()
