import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global check_marks
    window.after_cancel(timer)
    _title['text'] = 'Pomodoro'
    canvas.itemconfig(time, text='00:00')
    global reps
    reps = 0
    check_marks = ''
    _check_marks.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, check_marks
    work_rep = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        _title['text'] = 'Working'
        count_down(work_rep)
    elif reps == 2 or reps == 4 or reps == 6:
        check_marks += '✔'
        _check_marks.config(text=check_marks)
        _title['text'] = 'Short break'
        count_down(short_break)
    else:
        _title['text'] = 'Long Break'
        count_down(long_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count /60)
    count_sec = count % 60
    if count_sec < 10:
        canvas.itemconfig(time, text=f'{count_min}:0{count_sec}')
    else:
        canvas.itemconfig(time, text=f'{count_min}:{count_sec}')

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=90, pady=40, bg=YELLOW, )



# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
time = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1,row=1)

# count_down(10)

# Labels
_title = Label(text='Timer')
_title.config(font=(FONT_NAME,32), background=YELLOW, foreground=GREEN)
_title.grid(column=1, row=0)

_check_marks = Label(text=check_marks)
_check_marks.grid(column=1,row=4)
_check_marks.config(font=(FONT_NAME, 17), background=YELLOW, foreground=GREEN)

# Buttons
_button1 = Button(text='Start', highlightthickness=0, command=start_timer)
_button1.grid(column=0, row=3)

_button2 = Button(text='Reset', highlightthickness=0, command=reset_timer)
_button2.grid(column=2, row=3)

window.mainloop()
