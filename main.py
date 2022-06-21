from cgitb import text
from itertools import count
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", fg=GREEN)
    check_marks.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(long_break_sec)
        title_label.config(text="BREAK", fg=RED)
    elif REPS % 2 == 0:
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(short_break_sec)
        title_label.config(text="BREAK", fg=PINK)
    else:
        window.bell()
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(REPS/2)
        for i in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro !!")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()