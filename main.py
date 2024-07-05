from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash card game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
random_index = 0


def flip_card():
    canvas.itemconfig(guess_word, text=to_learn[random_index]["English"],fill="white")
    canvas.itemconfig(main_image, image=card_back_image)
    canvas.itemconfig(language_text, text="English",fill="white")


def new_word():
    global random_index, flip_timer
    window.after_cancel(flip_timer)
    random_index = random.randint(0, len(to_learn))
    canvas.itemconfig(guess_word, text=to_learn[random_index]["French"],fill="black")
    canvas.itemconfig(main_image, image=card_front_image)
    canvas.itemconfig(language_text, text="French",fill="black")
    flip_timer = window.after(3000,flip_card)

# ---------------------------- ELEMENTS SETUP ------------------------------- #
flip_timer = window.after(3000,flip_card)
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
main_image = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), text="French")
guess_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="trouve")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0, )
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

known_button = Button(image=right_image, highlightthickness=0, command=new_word)
unknown_button = Button(image=wrong_image, highlightthickness=0, command=new_word)

known_button.grid(row=1, column=0)
unknown_button.grid(row=1, column=1)
new_word()
count = 0


window.mainloop()
