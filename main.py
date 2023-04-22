import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TEXT = "the term computer language is sometimes used interchangeably with programming\nlanguage However the usage of\n" \
       "both terms varies among authors including the exact scope of each One\nusage describes programming languages as\n" \
       " a subset of computer languages similarly languages used in computing \nthat have a different goal than\n " \
       "expressing computer programs are generically designated computer languages \nfor instance, markup languages are\n " \



def count_speed(count):
     if count <= 60:
              word_count = len(TEXT.split())
              user_entry = len((entry.get()).split())
              if count > 0:
                     WPM = round((user_entry / count)*60, 2)
                     accuracy = len(set((entry.get()).split()) & set(TEXT.split()))
                     accuracy = round((accuracy / word_count),2)

                     wpm_label.config(text=f'WPM: {WPM}\n Accuracy: {accuracy}')
                     timer_label.config(text=f"Time: {count}s")
              timer = window.after(1000, count_speed, count + 1)
def start():
       count_speed(0)






window = Tk()
window.title("Typing Speed Test")
window.config(padx=100, pady=50, bg=YELLOW)
# window.geometry('1000x600')

title_label = Label(text="Typing Speed Test", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=1000, height=300, bg=YELLOW, highlightthickness=0)
test_text = canvas.create_text(500, 150, text=TEXT, fill=RED, font=(FONT_NAME, 16, 'bold'))

canvas.grid(column=1, row=1)

btn = Button(text='START', command=start)
btn.grid(column=0, row=2)
btn2 = Button(text="Reset")
btn2.grid(column=3, row=2)
entry = Entry(width=100)
entry.grid(column=1, row=3)

wpm_label = Label(text='WPM: ?\n Accuracy: ?', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
wpm_label.grid(column=0, row=3)
timer_label = Label(text='TIME: 00:00', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
timer_label.grid(column=3, row=3)

window.mainloop()
