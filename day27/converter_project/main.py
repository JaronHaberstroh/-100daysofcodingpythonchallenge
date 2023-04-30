import tkinter


def convert():
    conversion = round(float(user_input.get()) * 1.609, 2)
    result.config(text=conversion)


window = tkinter.Tk()
window.title("Unit Converter")
# window.minsize(height=100, width=200)
window.config(padx=30, pady=30)

user_input = tkinter.Entry(width=10, justify="right")
user_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equals_label = tkinter.Label(text="is equal to")
equals_label.grid(row=1, column=0)

result = tkinter.Label(text="0")
result.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

result_button = tkinter.Button(text="Calculate", command=convert)
result_button.grid(row=2, column=1)

window.mainloop()
