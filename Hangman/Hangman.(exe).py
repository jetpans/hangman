import tkinter as tk
from tkinter.font import Font
import os
from PIL import ImageTk, Image
import random

text_file = open("wordlist.txt","r")
wordlist = text_file.read().split("\n")

def reset():
    global letter
    global riddle
    global process
    global currentGuess
    global keyButtons
    global death
    global state
    global hanging
    global image
    global permaRiddle
    keyButtons = []
    riddle = list(wordlist[random.randint(0, len(wordlist)-1)].upper())
    permaRiddle = "".join(riddle[:])
    process = list("_ " * len(riddle))
    death = 6
    for widget in root.winfo_children():
        widget.destroy()
    state = "states/state_{}.png".format(6 - death)
    hanging = ImageTk.PhotoImage(Image.open(state))
    image = tk.Label(root, image=hanging, background="white")
    image.place(x=600, y=60)

    currentGuess = tk.StringVar()
    currentGuess.set("".join(process))

    guess = tk.Label(root, textvariable=currentGuess, font=myFont1)
    guess.place(x=keyboardX, y=keyboardY - 250)
    guess.configure(background="white")
    keyButtons = []

    for i in range(len(keyboard)):
        keyButtons.append([])
        for j in range(len(keyboard[i])):
            tempBut = tk.Button(root, text=keyboard[i][j], font=myFont2, height=1, width=3,
                                command=lambda word = keyboard[i][j], i=i, j=j: keyInput(word, i, j))

            keyButtons[i].append(tempBut)
            keyButtons[i][j].place(x=keyboardX + j * butH, y=keyboardY + i * butW)

def keyInput(a,i,j):
    global letter
    global riddle
    global process
    global currentGuess
    global keyButtons
    global death
    global state
    global hanging
    global image
    tempRiddle = riddle[:]
    letter = a
    if letter in riddle:
        for g in (range(riddle.count(letter))):
            process[riddle.index(letter)*2] = letter
            riddle[riddle.index(letter)] = "//"
    else:
        death -= 1
        state = "states/state_{}.png".format(6 - death)
        hanging = ImageTk.PhotoImage(Image.open(state))
        image = tk.Label(root, image=hanging, background="white")
        image.place(x=600, y=60)
        if 6-death == 7:
            for widget in root.winfo_children():
                widget.destroy()
            deathWin = tk.Label(root, text="You lost!", background = "white", font=Font(family="Calibri", size=100),fg="red")
            deathWin1 = tk.Label(root, text="The word was {}.".format(permaRiddle), background="white", font=Font(family="Calibri", size=50), fg="purple")
            deathWin.place(relx=0.5, y=100, anchor="center")
            deathWin1.place(x=0,y=200)
            playAgain = tk.Button(root, text="I want to play again!", background="white", font=Font(family="Calibri", size=50),fg="blue",command=reset)
            playAgain.place(x=0,y=500)
            state = "states/state_{}.png".format(6 - death)
            hanging = ImageTk.PhotoImage(Image.open(state))
            image = tk.Label(root, image=hanging, background="white")
            image.place(x=650, y=300)
    if "_" not in process:
        for widget in root.winfo_children():
            widget.destroy()
        deathWin = tk.Label(root, text="You won!", background = "white", font=Font(family="Calibri", size=100),fg="red")
        deathWin1 = tk.Label(root, text="You only messed up {} times.".format(6-death), background="white", font=Font(family="Calibri", size=50), fg="purple")
        deathWin.place(x=200, y=0)
        deathWin1.place(x=200,y=200)
        playAgain = tk.Button(root, text="I want to play again!", background="white", font=Font(family="Calibri", size=50),fg="blue",command=reset)
        playAgain.place(x=200,y=500)
    keyButtons[i][j].configure(fg="gray", state="disabled")
    keyButtons[i][j].place(x=keyboardX + j * butH, y=keyboardY + i * butW)
    currentGuess.set("".join(process))
    print(process)
    print(riddle)
    print(a)


riddle = list(wordlist[random.randint(0, len(wordlist)-1)].upper())
permaRiddle = "".join(riddle[:])
process = list("_ " * len(riddle))
death = 6

keyboard = []
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphaCopy = alphabet[:]
keyboardX = 100
keyboardY = 500
for i in range(2):
    keyboard.append([])
    for j in range(10):
        keyboard[i].append(alphabet[10*i + j])
        alphaCopy.remove(alphabet[10*i + j])
keyboard.append(alphaCopy)

butH = 70
butW = 70


root = tk.Tk()
root.geometry("1024x768")
root.configure(background="white")

myFont1 = Font(family="Calibri", size=50)
myFont2 = Font(family="Calibri", size=20)
state = "states/state_{}.png".format(6-death)
hanging = ImageTk.PhotoImage(Image.open(state))
image = tk.Label(root, image=hanging, background = "white")
image.place(x=600, y=60)

currentGuess = tk.StringVar()
currentGuess.set("".join(process))

guess = tk.Label(root, textvariable=currentGuess, font=myFont1)
guess.place(x=keyboardX, y=keyboardY - 250)
guess.configure(background="white")
keyButtons = []

for i in range(len(keyboard)):
    keyButtons.append([])
    for j in range(len(keyboard[i])):
        tempBut = tk.Button(root, text=keyboard[i][j], font=myFont2, height=1, width=3, command=lambda word=keyboard[i][j], i=i, j=j: keyInput(word,i,j))
        keyButtons[i].append(tempBut)
        keyButtons[i][j].place(x=keyboardX + j*butH, y=keyboardY + i*butW)

root.mainloop()
