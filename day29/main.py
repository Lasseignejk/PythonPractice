from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(nr_letters)]

    password_list += [choice(symbols) for _ in range(nr_symbols)]

    password_list += [choice(numbers) for _ in range(nr_numbers)]

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    
    # pyperclip allows us to copy things to the clipboard automatically.
    pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_text = website_input.get()
    email_text = email_input.get()
    password_text= password_input.get()

    if website_text == "" or password_text == "":
        messagebox.showerror(title="Oh no!", message="Please make sure that all fields are filled out.")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered: \nWebsite: {website_text} \nEmail: {email_text} \nPassword: {password_text} \nDo you want to save this info?")

        if is_ok:
            with open("day29/data.txt", mode="a") as file:
                file.write(f"\n{website_text} | {email_text} | {password_text}")
            website_input.delete(0,'end')
            password_input.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="day29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_input = Entry(width=52)
email_input.insert(0, "jaye@email.com")
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input=Entry(width=33)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()