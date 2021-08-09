from tkinter import *
import pandas
import random

global current_card
global flip_timer



BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Ariel'

data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")

def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)

    canvas.itemconfig(current_language, text='French', fill='black')
    canvas.itemconfig(current_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_photo)

    flip_timer = window.after(3000, func=card_flip)

def card_flip():

    canvas.itemconfig(card_background, image=card_back_photo)
    canvas.itemconfig(current_language, text='English', fill='white')
    canvas.itemconfig(current_word, text=current_card['English'], fill='white')


window = Tk()
window.title('Flashcard App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_photo = PhotoImage(file="images/card_front.png")
card_back_photo = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_photo)
canvas.grid(column=0, row=0, columnspan=2)

current_language = canvas.create_text(400, 150, text="", fill='black', font=(FONT, 40, 'italic'))
current_word = canvas.create_text(400, 263, text="", fill='black', font=(FONT, 60, 'bold'))

right_photo = PhotoImage(file="images/right.png")
wrong_photo = PhotoImage(file="images/wrong.png")

right_btn = Button(image=right_photo, highlightthickness=0, command=new_word)
wrong_btn = Button(image=wrong_photo, highlightthickness=0, command=new_word)

right_btn.grid(column=1, row=1)
wrong_btn.grid(column=0, row=1)

flip_timer = window.after(3000, func=card_flip)

new_word()


window.mainloop()


