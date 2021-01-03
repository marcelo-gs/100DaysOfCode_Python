##Import zone
import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SEGUNDS = 60
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    check_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def addChecked():
    """ ✔  ✔️"""
    check_label.config(text=check_label['text'] + " ✔")

def start():
    global reps
    reps += 1

    ##DEBUG VARIABLE
    #SEGUNDS = 1
    #WORK_MIN = 2
    #SHORT_BREAK_MIN = 1
    #LONG_BREAK_MIN = 2
    ##DEBUG VARIABLE

    if reps % 8 == 0:
        long_break_seg = LONG_BREAK_MIN * SEGUNDS
        timer_label.config(fg=RED, text="Break")
        count_down(long_break_seg)
    elif reps % 2 == 0:
        short_break_seg = SHORT_BREAK_MIN * SEGUNDS
        timer_label.config(fg=PINK, text="Break")
        count_down(short_break_seg)
    else:
        work_seg = WORK_MIN * SEGUNDS
        timer_label.config(fg=GREEN, text="Work")
        count_down(work_seg)
    

def format_timer(seg):
    minuts = math.floor(seg / 60)
    segunds = seg % 60
    display_minuts = str(minuts)
    display_seg = str(segunds)
    if minuts < 10:
        display_minuts = f"0{minuts}"
    if segunds < 10:
        display_seg = f"0{segunds}"
    return f"{display_minuts}:{display_seg}"
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=format_timer(count))
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 ==0:
            addChecked()
        start()
        
# ---------------------------- UI SETUP ------------------------------- #
#####Create objects
window = tkinter.Tk()
timer_label = tkinter.Label()
check_label = tkinter.Label()
canvas = tkinter.Canvas(width=210, height=228, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
start_button = tkinter.Button()
reset_button = tkinter.Button()

#####Setup Objects

#Window
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.after(1000, )

#Canvas
canvas.create_image(103,115, image=tomato_img)
timer_text = canvas.create_text(103,138, text="00:00", fill="white", font=(FONT_NAME,30, "bold"))

#Label
timer_label.config(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME,30, "bold"))
check_label.config(fg=GREEN, bg=YELLOW, text="", font=(FONT_NAME,12, "normal"))

#Button
start_button.config(text="Start", command=start)
reset_button.config(text="Reset", command=reset)

#####Positions
timer_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_label.grid(column=1, row=3)


#Mainloop
window.mainloop()
