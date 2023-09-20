from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
timer = None
random_card = None

# -------------------------- CREATE CARDS -------------------------

data = pandas.read_csv("day31/flash_card_capstone_project/data/japanese_words.csv")
data_dict = data.to_dict(orient="records")


def get_random_card(): 
    global timer
    global random_card
    random_card = random.choice(data_dict)
    canvas.itemconfig(target_lang, text="Japanese")
    canvas.itemconfig(target_word, text=random_card["Japanese"])
    timer = window.after(2000, flip_card)

# -------------------------- FLIP CARDS -------------------------
def flip_card():
    canvas.itemconfig(card_side, image=back_img)
    canvas.itemconfig(target_lang, text="English", fill="white")
    canvas.itemconfig(target_word, text=random_card["English"], fill="white")
    window.after_cancel(timer)
    

# ------------------------------- UI ---------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="day31/flash_card_capstone_project/images/card_front.png")
card_side = canvas.create_image(400, 263, image=front_img)

back_img = PhotoImage(file="day31/flash_card_capstone_project/images/card_back.png")


target_lang = canvas.create_text(400, 150, 
                                 text="target lang", 
                                 fill="black", 
                                 font=("Ariel", 40, "italic"))
target_word = canvas.create_text(400, 263, 
                                      text="word", 
                                      fill="black", 
                                      font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="day31/flash_card_capstone_project/images/wrong.png")
wrong_button = Button(highlightthickness=0, image=wrong_image, command=get_random_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="day31/flash_card_capstone_project/images/right.png")
right_button = Button(highlightthickness=0, image=right_image, command=get_random_card)
right_button.grid(column=1, row=1)

get_random_card()

window.mainloop()
