import tkinter
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Courier"
WRITE_YOUR_EMAIL = "example.gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    [password_list.append(random.choice(letters)) for let in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for sym in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for num in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join(password_list)
    input_pass.delete(0, "end")
    input_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = input_website.get()
    email = input_email.get()
    password = input_pass.get()
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        ask_ok = messagebox.askokcancel(title=website,
                                        message=f"There are the details entered: \n"
                                                f"Email: {email}\n"
                                                f"Password: {password} \n Is it ok to save?")

        if ask_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"\n{website} | {email} | {password}")
            input_website.delete(0, "end")
            input_pass.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("PassWord Manager")
window.config(padx=50, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

w_website = tkinter.Label(text="Website:")
w_website.grid(row=1, column=0)

w_email = tkinter.Label(text="Email/Username:")
w_email.grid(row=2, column=0)

w_password = tkinter.Label(text="Password:")
w_password.grid(row=3, column=0)

input_website = tkinter.Entry(width=45)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

input_email = tkinter.Entry(width=45)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, WRITE_YOUR_EMAIL)

input_pass = tkinter.Entry(width=27)
input_pass.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
