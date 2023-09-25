from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.breakingbadquotes.xyz/v1/quotes")
    
    response.raise_for_status()
    data = response.json()
    if len(data) <= 70:
        canvas.itemconfig(quote_text, text=data[0]["quote"])
    else:
        get_quote()



window = Tk()
window.title("Breaking Bad says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day33/breaking_bad_quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Hit the button", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)


quote_button = Button(text="Get Quote", highlightthickness=0, command=get_quote)
quote_button.grid(row=1, column=0)



window.mainloop()