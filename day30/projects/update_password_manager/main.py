import tkinter
import json
from tkinter import messagebox
from random import choice, randint, shuffle

FONT = ("Times New Roman", 12, "normal")
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def find_password(event=None):
    dict_key = website.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found",
                             message="No file containing password info.")
    else:
        if dict_key in data:
            data_user = data[dict_key]["email/username"]
            data_pass = data[dict_key]["password"]
            messagebox.showinfo(
                title=dict_key, message=f"{data_user}\npassword: {data_pass}")
        else:
            messagebox.showerror(title="Save data not found",
                                 message="No info found for given website.")


# -------------------------- PASSWORD GENERATOR ----------------------------- #


def generate_password(event=None):
    password_list = [choice(LETTERS) for _ in range(randint(8, 10))]
    password_list += [choice(SYMBOLS) for _ in range(randint(2, 4))]
    password_list += [choice(NUMBERS) for _ in range(randint(2, 4))]
    shuffle(password_list)
    generated_pass = "".join(password_list)

    pass_input.delete(0, "end")
    pass_input.insert(0, generated_pass)

    pass_input.clipboard_clear()
    pass_input.clipboard_append(generated_pass)
    pass_input.update()

# -------------------------- SAVE PASSWORD ----------------------------- #


def save(event=None):
    new_data = {
        website.get(): {
            "email/username": username.get(),
            "password": password.get(),
        }
    }
    if website.get() == "" or username.get() == "" or password.get() == "":
        messagebox.showinfo(
            title="Missing Fields", message="Please complete all fields.")
    else:
        confirmed = messagebox.askokcancel(
            title="Confirm", message="Would you like to confirm")
        if confirmed:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = new_data
            else:
                data.update(new_data)
            finally:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                web_input.delete(0, 'end')
                pass_input.delete(0, 'end')

# -------------------------- UI SETUP ----------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
window.bind("<Control-p>", generate_password)
window.bind("<Control-f>", find_password)
window.bind('<Control-s>', save)

canvas = tkinter.Canvas(width=200, height=200)
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

web_label = tkinter.Label(text="Website:")
web_label.grid(row=1, column=0)

user_label = tkinter.Label(text="Email/Username:")
user_label.grid(row=2, column=0)

pass_label = tkinter.Label(text="Password:")
pass_label.grid(row=3, column=0)

website = tkinter.StringVar()
web_input = tkinter.Entry(width=25, textvariable=website)
web_input.focus()
web_input.grid(row=1, column=1)

username = tkinter.StringVar()
user_input = tkinter.Entry(width=45, textvariable=username)
user_input.insert(0, "Test@gmail.com")
user_input.grid(row=2, column=1, columnspan=2)

password = tkinter.StringVar()
pass_input = tkinter.Entry(width=26, textvariable=password)
pass_input.grid(row=3, column=1)

search_button = tkinter.Button(width=16, text="Search", command=find_password)
search_button.grid(row=1, column=2)

pass_gen_button = tkinter.Button(
    text="Generate Password", command=generate_password)
pass_gen_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
