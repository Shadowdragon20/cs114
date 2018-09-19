from tkinter import *

class Window(Frame):
    def _init_(self, master=None):
        Frame._init_(self, master)
        self.master = master

root =Tk()
app = Window(root)
root.mainloop()
