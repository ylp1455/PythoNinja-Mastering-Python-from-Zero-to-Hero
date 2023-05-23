from tkinter import *
from tkinter import filedialog

def saveFile():
   file =  filedialog.asksaveasfile()
   

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
