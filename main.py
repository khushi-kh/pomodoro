from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
D_GREEN = "#379b46"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", font=(FONT_NAME, 62, "bold"), fg=GREEN, bg=YELLOW)
    timer_label.place(x=0, y=-85)
    canvas.itemconfig(timer_count, text="00:00")
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 7 == 0 and reps != 0:
        countdown(long_break_sec)
        timer_label.config(text="Take A Break", font=(FONT_NAME, 50, "bold"), foreground=RED)
        timer_label.place(x=-115, y=-75)
    elif reps % 2 == 0:
        countdown(work_sec)
        timer_label.config(text="Work Hard", font=(FONT_NAME, 60, "bold"), foreground=D_GREEN)
        timer_label.place(x=-95, y=-85)
    elif reps % 2 == 1:
        countdown(short_break_sec)
        timer_label.config(text="A Short Break", font=(FONT_NAME, 45, "bold"), foreground=PINK)
        timer_label.place(x=-108, y=-75)

    reps += 1


# --------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer

    count_min = count // 60
    count_sec = round(count % 60)
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_label.config(text=marks)
    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=120, pady=120, bg=YELLOW)

canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato_img)
timer_count = canvas.create_text(125, 147, text="00:00", fill=YELLOW, font=(FONT_NAME, 28, "bold"))
canvas.pack()

timer_label = Label(text="Timer", font=(FONT_NAME, 62, "bold"), fg=GREEN, bg=YELLOW)
timer_label.place(x=0, y=-85)

start_button = Button(text="Start", fg="blue", font=(FONT_NAME, 15, "normal"), highlightthickness=0,
                      command=start_timer)
start_button.place(x=0, y=250)

reset_button = Button(text="Reset", fg="blue", font=(FONT_NAME, 15, "normal"), highlightthickness=0, command=reset)
reset_button.place(x=200, y=250)

check_label = Label(text="", font=(FONT_NAME, 15, "normal"), fg=D_GREEN, bg=YELLOW)
check_label.place(x=95, y=250)

window.mainloop()
