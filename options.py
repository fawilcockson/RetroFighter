import tkinter
from tkinter import *
import os
import json


window = tkinter.Tk()
window.title("Retro Fighter")
window.geometry("1000x600")
window.resizable(True, True)

# Create a dropdown list for the options for resolution
resolution = tkinter.StringVar()
resolution.set("Resolution")
resolutionMenu = tkinter.OptionMenu(window, resolution, "800x600", "1024x768", "1280x720", "1366x768", "1600x900",
                                    "1920x1080")
print(resolution.get())
resolutionMenu.place(x=0, y=0)

# Create a slider for the volume of the game
volume = tkinter.Scale(window, from_=0, to=100, orient=HORIZONTAL)
volume.place(x=0, y=50)

# Create a checkbox for the fullscreen option
fullscreen = tkinter.IntVar()
fullscreen.set(0)
fullscreenCheck = tkinter.Checkbutton(window, text="Fullscreen", variable=fullscreen)
fullscreenCheck.place(x=0, y=100)

# Create a set of print statements to print the values of the options
print("Resolution: " + resolution.get())
print("Volume: " + str(volume.get()))
print("Fullscreen: " + str(fullscreen.get()))

# Create a button to return the main menu
backButton = tkinter.Button(window, text="Back", command=lambda: [window.destroy(), os.system('py menu.py')], height=5,width=5)
backButton.pack(anchor=tkinter.E)

# Write the data to a JSON in a function
def writeJSON():
    dataToJSON = {
        "Resolution": resolution.get(),
        "Volume": volume.get(),
        "Fullscreen": fullscreen.get()
    }
    with open("retroFighter.cfg", "w") as outfile: outfile.write(json.dumps(dataToJSON))

# Create a button to apply the settings by writing them to retroFighter.cfg
applyButton = tkinter.Button(window, text="Apply",
                             command=lambda: [print("Applied"), writeJSON()], height=5,
                             width=5)
applyButton.pack(anchor=tkinter.E)

window.mainloop()