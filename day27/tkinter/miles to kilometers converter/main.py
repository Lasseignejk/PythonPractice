from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# There is an input field where the user can type in a number of miles to convert. Below, it says "is equal to 0 Km" and below that is a button that says "Calculate".
# When the button is clicked, the "is equal to" line should update to say 27 Km or whatever.
# To go from miles to km, multiply the miles by 1.609.

# Input
input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

# Input label
input_label = Label(text="Miles", font=("Arial", 10))
input_label.grid(column=2, row=0)

# answer label 1
is_equal_label = Label(text="is equal to", font=("Arial", 10))
is_equal_label.grid(column=0, row=1)

# answer label 2 (part that will update)
answer_label = Label(text="0", font=("Arial", 10))
answer_label.grid(column=1, row=1)

# answer label 2, km
km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

# Button
def convert_miles():
    user_input = input.get()
    answer = round(float(user_input) * 1.609)
    answer_label["text"] = f"{answer}"

calculate_button = Button(text="Calculate", command=convert_miles)
calculate_button.grid(column=1, row=2)




window.mainloop()