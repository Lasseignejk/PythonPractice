from tkinter import Tk, Canvas, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------- UI ---------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="day31/flash_card_capstone_project/images/card_front.png")
canvas.create_image(400, 263, image=front_img)
target_lang = canvas.create_text(400, 150, 
                                 text="Japanese", 
                                 fill="black", 
                                 font=("Ariel", 40, "italic"))
target_lang_text = canvas.create_text(400, 263, 
                                      text="家族", 
                                      fill="black", 
                                      font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="day31/flash_card_capstone_project/images/wrong.png")
wrong_button = Button(highlightthickness=0, image=wrong_image)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="day31/flash_card_capstone_project/images/right.png")
right_button = Button(highlightthickness=0, image=right_image)
right_button.grid(column=1, row=1)

window.mainloop()
