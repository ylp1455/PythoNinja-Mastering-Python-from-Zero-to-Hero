# widget  = GUI elements: buttons, labels,textboxes,image_names
# windows = serve as a container to hold or contain theese widgets

from tkinter import *


window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("ylp first gui ")

icon = PhotoImage(file = 'images/logo.png' )
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop() #place windows on computer screen , listen for events


