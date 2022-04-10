from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


try:
    database_words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    database_words = pandas.read_csv("data/english_words.csv")

all_words = database_words.to_dict("records")

random_dict = {}
words_to_learn = []




#------------------------- Functions -------------------------------


def random_word():
    global random_dict
    random_dict = random.choice(all_words)
    english_word = random_dict["English"]
    russian_word = random_dict["Russian"]
    return english_word, russian_word

def show_russian(word):
    canvas.itemconfig(work_image, image=front_image)
    canvas.itemconfig(window_language, text="Russian")
    canvas.itemconfig(window_word, text=word)

def show_english(word):
    canvas.itemconfig(work_image, image=back_image)
    canvas.itemconfig(window_language, text="English")
    canvas.itemconfig(window_word, text=word)

def show_random_word():
    english, russian = random_word()
    show_english(english)
    window.after(3000, show_russian, russian)


def know_word():
    all_words.remove(random_dict)
    data = pandas.DataFrame(all_words)
    data.to_csv("data/words_to_learn.csv", index=False)
    print(len(all_words))
    show_random_word()



#-------------------------UI setting -------------------------------
# create work window
window = Tk()
window.title("Easy way to learn English")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


# create canvas and setup background color
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)

# create image objects
back_image = PhotoImage(file="./images/card_back.png")
front_image = PhotoImage(file="./images/card_front.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

# creating image on the work window
work_image = canvas.create_image(400, 265, image=front_image)

# place on the grid
canvas.grid(column=0, row=0, columnspan=2)

# creating text
window_language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
window_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# creating buttons
right_button = Button(image=right_image, highlightthickness=0, command=know_word)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=show_random_word)

# place buttons on the grid
right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)

show_random_word()



#---------------------------------------------------------------------------


window.mainloop()
