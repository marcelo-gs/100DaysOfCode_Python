import tkinter
from tkinter import messagebox
import random
import pandas

timer = None
words = []

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

LINE1_FONT =(FONT_NAME,35, "italic")
LINE2_FONT=(FONT_NAME,50, "bold")

def change_side():
    canvas.itemconfig(canvas_img, image=img_cardBack)
    canvas.itemconfig(canvas_line1, text="English", fill="white")
    canvas.itemconfig(canvas_line2, text=words[-1]["English"], fill="white")
    window.after_cancel(timer)

def right_onClick():
    global timer
    timer = window.after(3000, change_side)
    DATA.remove(words[-1])
    data = pandas.DataFrame(DATA)
    data.to_csv("data/words_to_learn.csv")
    random_info()

def wrong_onClick():
    global timer
    timer = window.after(3000, change_side)
    random_info()

def random_info():
    global words
    if len(DATA) == 0:
        canvas.itemconfig(canvas_line1, text="It's all for today")
        canvas.itemconfig(canvas_line2, text="You finish all cards.")
        window.after_cancel(timer)
        btn_right.config(command=None)
        btn_wrong.config(command=None)
    else:
        choice_word = random.choice(DATA)
        words.append(choice_word)
        canvas.itemconfig(canvas_img, image=img_cardFront)
        canvas.itemconfig(canvas_line1, text="French", fill="black")
        canvas.itemconfig(canvas_line2, text=choice_word["French"], fill="black")

def readData():
    try:
        data = pandas.read_csv('data/words_to_learn.csv')
        #data_dict = {row["French"]:row["English"] for (index, row) in data.iterrows()}    
    except FileNotFoundError:
        data = pandas.read_csv('data/french_words.csv')
        
    finally:
        data_dict = data.to_dict(orient="records")

    if len(data_dict) == 0:
        data = pandas.read_csv('data/french_words.csv')
        data_dict = data.to_dict(orient="records")
    return data_dict

DATA = readData()

#####Create objects
window = tkinter.Tk()

canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)

img_cardBack = tkinter.PhotoImage(file="images/card_back.png")
img_cardFront = tkinter.PhotoImage(file="images/card_front.png")
img_right = tkinter.PhotoImage(file="images/right.png")
img_wrong = tkinter.PhotoImage(file="images/wrong.png")

btn_right = tkinter.Button()
btn_wrong = tkinter.Button()

#####Setup Objects
#Window
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
canvas_img = canvas.create_image(400,263, image=img_cardFront)
canvas_line1 = canvas.create_text(400,150, text="Line 1", fill="black", font=LINE1_FONT)
canvas_line2 = canvas.create_text(400,263, text="Line 2", fill="black", font=LINE2_FONT)
canvas.config(bg=BACKGROUND_COLOR)

#Button
btn_right.config(image=img_right, command=right_onClick, highlightthickness=0)
btn_wrong.config(image=img_wrong, command=wrong_onClick, highlightthickness=0)

#####Positions
#line 1 
canvas.grid(row=0, column=0, columnspan=2)

#line 2
btn_right.grid(row=1, column=0)
btn_wrong.grid(row=1, column=1)

timer = window.after(3000, change_side)
random_info()
window.mainloop()