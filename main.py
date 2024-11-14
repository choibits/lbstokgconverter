from tkinter import *

# WINDOW
window = Tk()
window.title("Lbs to kgs converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

# LABEL
header = Label(text="Converter", font=("Arial", 14, "bold"))
header.grid(column=1, row=0)

# INPUT
entry = Entry(width=7)
entry.grid(column=1, row=1)


# BUTTON
def convert():
    lbs = float(entry.get())
    kgs = round(lbs * 0.45359237)
    kgs_result_label.config(text=f"{kgs}")


button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=2)

pounds_label = Label(text="Lbs")
pounds_label.grid(column=2, row=1)

kgs_label = Label(text="Kgs")
kgs_label.grid(column=2, row=2)

kgs_result_label = Label(text="0")
kgs_result_label.grid(column=1, row=2)

window.mainloop()

