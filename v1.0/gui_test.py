#pip install tk
#from curses import window
from cProfile import label
import tkinter

window = tkinter.Tk()

window.minsize(400,400)

window.title("Application name")

window.wm_iconbitmap("hackerman.png")

label = tkinter.Label(window, text="Hello world")

label.place(x=10, y=10)

button = tkinter.Button(window, text="click here")

button.place(x=10, y=20)

window.mainloop()