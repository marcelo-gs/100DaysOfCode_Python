from tkinter import * 
def calculate():
   value_label['text'] =  str(round(float(input_entry.get()) * 1.609,2))

#Create elements
window = Tk()
window.title("Mile to Km Converter")
window.minsize()
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
input_entry = Entry(width=10)
equals_label = Label(text="is equal to")
value_label = Label(text="0")
km_label = Label(text="Km")
button = Button(text="Calculate", command=calculate)

#positions
input_entry.grid(column=2, row=0)
miles_label.grid(column=3, row=0)

equals_label.grid(column=1, row=1)
value_label.grid(column=2, row=1)
km_label.grid(column=3, row=1)

button.grid(column=2, row=2)

window.mainloop()