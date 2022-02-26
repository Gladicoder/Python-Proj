from tkinter import *
from tkinter import messagebox
import random

colours1 = ['Red', 'Blue', 'Green', 'Pink', 'Black','Yellow', 'Orange', 'White']

colours2 = ['Red', 'Blue', 'Green', 'Pink', 'Black','Yellow', 'Orange', 'White', 'Purple', 'Brown', 'Cyan']
score1 = score2 = 0
timeleft1 = 30
timeleft2 = 60

def start1(event):
    if timeleft1 == 30:
        count1()
    ColourShuffle1()

def ColourShuffle1():
    global score1
    global timeleft1
    if timeleft1 > 0:
        if e1.get().lower() == colours1[3].lower():
            score1 += 1
        e1.delete(0, END)
        random.shuffle(colours1)
        label1.config(fg=str(colours1[3]), text=str(colours1[1]))
        scoreTab1.config(text="Score: " + str(score1))

def count1():
    global timeleft1

    if timeleft1 > 0:
        timeleft1 -= 1

        timeTab1.config(text="You have: " + str(timeleft1) + " second/s")
        timeTab1.after(1000, count1)

def start2(event):
    if timeleft2 == 60:
        count2()
    ColourShuffle2()
def ColourShuffle2():
    global score2

    global timeleft2
    global e2, label2, scoreTab2

    if timeleft2 > 0:
        if e2.get().lower() == colours2[0].lower():
            score2 += 1

        e2.delete(0, END)

        random.shuffle(colours2)

        label2.config(fg=str(colours2[0]), text=str(colours2[1]))
        scoreTab2.config(text="Score: " + str(score2))

def count2():
    global timeleft2, timeTab2

    if timeleft2 > 0:
        timeleft2 -= 1
        timeTab2.config(text="You have: " + str(timeleft2) + " second/s")
        timeTab2.after(1000, count2)

root = Tk()
root.title("The Color Game: Beginner Level")
root.geometry("390x265")

instruction1 = Label(root, text="Tell the colour of the word, and not the word!", font=('Helvetica', 12, "bold"),fg="red")
instruction1.pack()
scoreTab1 = Label(root, text="Try scoring more than 10! Hit enter to start playing!", font=('Helvetica', 12, "bold"),fg="red")
scoreTab1.pack()
timeTab1 = Label(root, text="You have: " + str(timeleft1) + " second/s", font=('Helvetica', 12, "bold"), fg="dark red")
timeTab1.pack()
label1 = Label(root, font=('Times', 65, "bold"))
label1.pack()
e1 = Entry(root, relief=GROOVE)
e1.pack()
root.bind('<Return>', start1)

def info():
    messagebox.showinfo("The Stroop Effect Experiment",'''In psychology, the Stroop effect is the delay in reaction time between congruent and incongruent stimuli.A basic task that demonstrates this effect occurs when there is a mismatch between the name of a color (e.g., "blue", "green", or "red") and the color it is printed on (i.e., the word "red" printed in blue ink instead of red ink). When asked to name the color of the word it takes longer and is more prone to errors when the color of the ink does not match the name of the color. The higher you score, the better is your selective attention and speed of processing various information!''')

def open_new():
    global scoreTab2, timeTab2, label2, e2
    window = Toplevel()
    window.geometry("460x220")
    window.title("The Color Game: Advance Level")
    instruction2 = Label(window, text="Lengthier the game, the more confusing it will get!",
                         font=('Helvetica', 12, "bold"), fg="red")
    instruction2.pack()

    scoreTab2 = Label(window, text="Hit enter to start playing!", font=('Helvetica', 12, "bold"), fg="red")
    scoreTab2.pack()

    timeTab2 = Label(window, text="You have: " + str(timeleft2) + " second/s", font=('Helvetica', 12, "bold"),
                     fg="dark red")
    timeTab2.pack()

    label2 = Label(window, font=('Times', 65, "bold"))
    label2.pack()

    e2 = Entry(window, relief=GROOVE)
    e2.pack()

    exit2 = Button(window, text="Exit", padx=20, command=window.destroy).place(anchor=SW, x=30, y=200)

    window.bind('<Return>', start2)

exit1 = Button(root, text="Exit", padx=20, command=root.destroy).place(anchor=SW, x=30, y=200)
adv = Button(root, text="Advance", padx=20, command=open_new).place(anchor=SE, x=370, y=200)
Button(root, text="INFO!", command=info).place(anchor=S, x=200, y=250)

root.mainloop()



