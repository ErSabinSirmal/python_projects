from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ------Random French words -------------#
def next_card():
    # random_word = data_dict[random.randint(0, len(data_dict))]["French"]
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=f"{current_card["French"]}",fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

# ------------Flip Card -----------------#
def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=back_img)

# -------------- Save Progress --------------#
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()





# --------UI DESIGN ---------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)
canvas = Canvas(width=800, height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(402, 263,image=front_img)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))

canvas.grid(column=0, row=0,columnspan=2)


#Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
cancel_button = Button(image=wrong_img, highlightthickness=0,borderwidth=0,command=next_card)
cancel_button.grid(column=0,row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0,borderwidth=0,command=is_known)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()
