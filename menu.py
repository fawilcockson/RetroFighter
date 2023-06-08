import tkinter as tk
from tkinter import *
import os


# Create a window
window = tk.Tk()
window.title("Retro Fighter")
window.geometry("1000x600")
window.resizable(True, True)

# Make the buttons
button1 = tk.Button(window, text="Fight!", command=lambda: [window.destroy(), os.system('py characterSelect.py')], height=5, width=50)
button2 = tk.Button(window, text="Quit", command=window.destroy, height=5, width=50)
button3 = tk.Button(window, text="Options", command=lambda: [window.destroy(), os.system('py options.py')], height=5, width=50)
button1.place(x=0, y=100)
button2.place(x=0, y=300)
button3.place(x=0, y=500)

# Create a label
retroLabel = tk.Label(window, text="Retro", font=("Impact", 108))
retroLabel.place(x=500, y=100)
retroLabel.config(fg="red", bg="black")
fighterLabel = tk.Label(window, text="Fighter", font=("Impact", 108))
fighterLabel.place(x=500, y=300)
fighterLabel.config(fg="blue", bg="black")


# Change the colours of everything
button1.config(fg="white", bg="red")
button2.config(fg="white", bg="blue")
button3.config(fg="white", bg="green")
window.config(bg="black")


# Run the mainloop
window.mainloop()