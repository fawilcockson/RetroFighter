import tkinter
from tkinter import *
import os
import json

# Initialise the window
window = tkinter.Tk()
window.title("Retro Fighter")
window.geometry("1000x600")
window.resizable(True, True)
window.configure(bg="black")

# Set some variables
characterData = {}
# Make the back button
backButton = tkinter.Button(window, text="Back", command=lambda: [window.destroy(), os.system('py menu.py')], height=5,
                            width=5)
backButton.place(x=0, y=10)

testButton = tkinter.Button(window, text="Fight!", command=lambda: [window.destroy(), os.system('py main.py')],
                            height=5,
                            width=5)
testButton.place(x=955, y=10)


def writeCharacterInfo(name):
    global characterData
    if name == "John":
        characterData = {
            "attack": 10,
            "spritePath": "assets/john.png",
            "punchSpritePath": "assets/johnPunch.png"
        }
    if name == "Steve":
        characterData = {
            "attack": 10,
            "spritePath": "assets/steve.png",
            "punchSpritePath": "assets/stevePunch.png"
        }
    if name == "Jacob":
        characterData = {
            "attack": 10,
            "spritePath": "assets/jacob.png",
            "punchSpritePath": "assets/jacobPunch.png"
        }

    with open("characters.cfg", "w") as outfile:
        outfile.write(json.dumps(characterData))

    updateCharacterText(name)


# Make a button for the basic character 'John'
johnButton = tkinter.Button(window, text="John", command=lambda: [writeCharacterInfo("John")])
johnButton.place(x=200, y=20)

# Add the image for John's character art
johnImage = tkinter.PhotoImage(file="assets/johnImage.png")
johnLabel = tkinter.Label(window, image=johnImage)
johnLabel.place(x=50, y=50)

# The same button for Steve
steveButton = tkinter.Button(window, text="Steve", command=lambda: [writeCharacterInfo("Steve")])
steveButton.place(x=500, y=20)

# Add the image for Steve's character art
steveImage = tkinter.PhotoImage(file="assets/steveImage.png")
steveLabel = tkinter.Label(window, image=steveImage)
steveLabel.place(x=350, y=50)

# another button for Jacob
jacobButton = tkinter.Button(window, text="Jacob", command=lambda: [writeCharacterInfo("Jacob")])
jacobButton.place(x=800, y=20)

# Add the image for Jacob's character art
jacobImage = tkinter.PhotoImage(file="assets/jacobImage.png")
jacobLabel = tkinter.Label(window, image=jacobImage)
jacobLabel.place(x=650, y=50)

# Add a label at the bottom which tells you which character is selected
characterChosen = Text(window, height=5, width=50)
characterChosen.place(x=300,y=500)
characterChosen.insert(END, "Character Chosen:")
characterChosen.config(fg="white", bg="black", font=("Impact", 20), border=0)


def updateCharacterText(character):
    characterChosen.delete("1.0", END)
    characterChosen.insert(END, "Character Chosen: " + character)


window.mainloop()