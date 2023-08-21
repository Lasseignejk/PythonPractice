from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked(): 
    my_label["text"] = input.get()

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# New Button
newButton = Button(text="I'm new")
newButton.grid(column=2, row=0)







window.mainloop()