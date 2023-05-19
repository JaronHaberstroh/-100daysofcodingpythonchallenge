import random
import pandas
import tkinter
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"

def save_on_close():
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    window.destroy()
        

def no_cards_error():
    messagebox.showerror(title="No index found", message="Flashcards completed.\nNo further cards in list to display.")
    
# window.cardinfo = [image_index, "French"/"English", data_index]
def draw_card():
    canvas.create_image(400, 263, image=window.images[window.cardinfo[0]])
    canvas.create_text(400, 163, text=window.cardinfo[1], font=("Ariel", 40, "italic"))
    try:
        canvas.create_text(400, 263, text=data_dict[window.cardinfo[1]][window.cardinfo[2]], font=("Ariel", 60, "bold"))
    except KeyError:
        no_cards_error()
    

def card_flip(event=None):
    if window.cardinfo[0] == 0:
        window.cardinfo[0] = 1
        window.cardinfo[1] = "English"
    else:
        window.cardinfo[0] = 0
        window.cardinfo[1] = "French"
    draw_card()

def correct_card(event=None):
    try:
        del data_dict["French"][window.cardinfo[2]]
        del data_dict["English"][window.cardinfo[2]]
    except KeyError:
        no_cards_error()
    new_card()

def new_card(event=None):
    window.cardinfo[0] = 0
    window.cardinfo[1] = "French"
    window.cardinfo[2] = random.choice(list(data_dict["French"].keys()))
    draw_card()


# Create data_dict
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict()
else:
    data_dict = data.to_dict()


# Window
window = tkinter.Tk()
window.title("Language Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.protocol("WM_DELETE_WINDOW", save_on_close)
window.cardinfo = [0, "French", 0]
window.images = []
window.images.append(tkinter.PhotoImage(file="images/card_front.png"))
window.images.append(tkinter.PhotoImage(file="images/card_back.png"))

# Create card image list

# Canvas
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
new_card()
canvas.grid(row=0, column=0, columnspan=2)
canvas.bind("<Button-1>", card_flip)

# Wrong Button
wrong_img = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, background=BACKGROUND_COLOR, padx=50, pady=50, command=new_card)
wrong_button.grid(row=1, column=0)

# Correct Button
correct_img = tkinter.PhotoImage(file="images/right.png")
correct_button = tkinter.Button(image=correct_img, highlightthickness=0, background=BACKGROUND_COLOR, padx=50, pady=50, command=correct_card)
correct_button.grid(row=1, column=1)


window.mainloop()
