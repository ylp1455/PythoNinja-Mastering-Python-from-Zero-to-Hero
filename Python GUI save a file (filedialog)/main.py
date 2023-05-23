from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = text.get(1.0, END)
    file.write(filetext)
    file.close()

window = Tk()
button = Button(window, text='Save', command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
