import tkinter

# window
window = tkinter.Tk()
window.title("My GUI")
window.minsize(width=500, height=300)
window.config(padx=30, pady=20)

# label
my_label = tkinter.Label(text="I am a label", font=("Sans", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)

# change label properties
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=10, pady=10)
# button


def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_2 = tkinter.Button(text="2nd button")
button_2.grid(column=2, row=0)

# entry
input = tkinter.Entry(width=10)
# input.pack()
# text = input.get()
input.grid(column=3, row=3)


# mainloop to keep window open
window.mainloop()
