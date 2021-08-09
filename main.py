from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = 'Ariel'


window = Tk()
window.title('Flashcard App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_photo = PhotoImage(file="images/card_front.png")
card_back_photo = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_photo)
canvas.grid(column=0, row=0, columnspan=2)

current_language = canvas.create_text(400, 150, text="Title", fill='black', font=(FONT, 40, 'italic'))
current_word = canvas.create_text(400, 263, text="word", fill='black', font=(FONT, 60, 'bold'))

right_photo = PhotoImage(file="images/right.png")
wrong_photo = PhotoImage(file="images/wrong.png")

right_btn = Button(image=right_photo, highlightthickness=0)
wrong_btn = Button(image=wrong_photo, highlightthickness=0)

right_btn.grid(column=1, row=1)
wrong_btn.grid(column=0, row=1)

window.mainloop()


