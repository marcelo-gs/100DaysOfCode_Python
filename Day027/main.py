from  tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

my_label = Label(text="I'm a Label", font=("Arial", 15, "bold"))
my_label.grid(column=0, row=0)
my_label['text'] = "new text"
my_label.config(text = "new text 2", padx=20, pady=20)


def button_clicked():
    my_label['text'] = input.get()

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me", command=button_clicked)
button2.grid(column=2, row=0)


#Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())






window.mainloop()
