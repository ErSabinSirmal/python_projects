from tkinter import *

def mile_to_kilometer():
    miles = float(input.get())
    km = round(miles * 1.609)
    kilometer_resul_label.config(text =f"{km}")
window = Tk()
window.title("Mile to Km converter")
# window.minsize(width=500, height= 500)
window.config(padx=20, pady= 20)


input = Entry(width= 10)
input.grid(column = 1, row = 0)


#labels
miles_label = Label(text ="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column =2, row = 0)

is_equal_to = Label(text ="is equal to ", font = ("Arial", 15, "normal"))
is_equal_to.grid(column = 0, row = 1)

kilometer_resul_label = Label(text = "0", font=("Arial", 15, "normal"))
kilometer_resul_label.grid(column = 1, row = 1)

km_label = Label(text ="Km", font=("Arial", 15, "normal"))
km_label.grid(column = 2, row = 1)


#Button
button = Button(text = "Calculate", font=("Arial", 15, "normal"),command=mile_to_kilometer)
button.grid(column = 1, row = 2)
window.mainloop()