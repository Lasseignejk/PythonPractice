from tkinter import Tk, Canvas, Entry, Label, PhotoImage, Button
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 
               'C', 'D', 'E', 'F', 'G', 'H', 'I', 
               'J', 'K', 'L', 'M', 'N', 'O', 'P', 
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
               'X', 'Y', 'Z']
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
    website_text = website_input.get().lower()
    email_text = email_input.get()
    password_text= password_input.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }

    if website_text == "" or password_text == "":
        messagebox.showerror(title="Oh no!", 
                             message="Please make sure that all fields are filled out.")
    else:
        try:
            with open("day29/password_manager/data.json", mode="r") as file:
                # Reading the old data
                data = json.load(file)

        except FileNotFoundError:
            with open("day29/password_manager/data.json", mode="w") as file:
                # Saving new data
                json.dump(new_data, file, indent=4)
                
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("day29/password_manager/data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
                
        finally:
            website_input.delete(0,'end')
            password_input.delete(0,'end')

# ---------------------------- SEARCH FOR INFO ------------------------------- #
def search_info():
    website = website_input.get().lower()
    if website == "":
        messagebox.showerror(title="Oh no!",
                             message="Please enter in a website.")
    else: 
        try: 
            with open("day29/password_manager/data.json", mode="r") as file:
                data = json.load(file)
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website.capitalize(),
                                    message=f"Email: {email}\nPassword: {password}")
        except FileNotFoundError:
            messagebox.showerror(title="Oh no!", 
                                 message="No data file found.")
        except KeyError:
            messagebox.showerror(title="Oh no!",
                                 message="No details for the website exist.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="day29/password_manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=33)
website_input.grid(column=1, row=1)
website_input.focus()

search_button = Button(text="Search", width=15, command=search_info)
search_button.grid(column=2, row=1)

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