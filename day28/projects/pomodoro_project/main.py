import tkinter
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
CHECKMARK = "✔"
reps = 0
timerr = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    timer_label.config(text="Timer")
    checkmarks.config(text="")

    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        time = LONG_BREAK_MIN  # * 60
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        time = SHORT_BREAK_MIN  # * 60
        timer_label.config(text="Break", fg=PINK)
    else:
        time = WORK_MIN  # * 60
        timer_label.config(text="Work", fg=GREEN)
    count_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            checkmarks.config(text=CHECKMARK * int(reps / 2))

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=40, pady=40, bg=YELLOW)
window.attributes('-topmost', True)

canvas = tkinter.Canvas(width=210, height=240, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(105, 120, image=tomato_img)
timer_text = canvas.create_text(105, 140, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(text="Timer", font=(
    FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = tkinter.Button(text="Start", font=(
    FONT_NAME, 20, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", font=(
    FONT_NAME, 20, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmarks = tkinter.Label(fg=GREEN,
                           bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks.grid(row=3, column=1)
window.mainloop()
