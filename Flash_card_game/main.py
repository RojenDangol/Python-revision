from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# Accessing the csv file
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
data_dict = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card, image=card_front)
    flip_timer = canvas.after(3000, func=flip_card)


def learned_word():
    data_dict.remove(current_card)
    df = pandas.DataFrame(data_dict)
    df.to_csv('data/words_to_learn.csv', index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


# UI
window = Tk()
window.title('Flash Card')
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

# images
card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(405, 263, image=card_front)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, func=flip_card)
# button
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)
right_btn = Button(image=right_img, highlightthickness=0, command=learned_word)
right_btn.grid(column=1, row=1)

next_card()
window.mainloop()