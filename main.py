from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashcard App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
tomato_photo = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=tomato_photo)
canvas.grid(column=0, row=0)


window.mainloop()


