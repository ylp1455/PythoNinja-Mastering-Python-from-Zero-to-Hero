from tkinter import *

# label = an area widget that holds text and/or an image wihin window


window = Tk()
window.geometry("200x200")

label =Label(window,  text="hello world")
label.pack()
label.place(x = 0 , y = 0)

window.mainloop()