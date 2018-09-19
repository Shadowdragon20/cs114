from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):
    def _init_frame(self, master = None):
        Frame. _init_(self, master)
        self.master = master
        self._init_window()
        return _init_frame()

    def _init_window(self):
        self.master.title('GUI')
        self.pack(fill=BOTH, expand=1)

        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=0, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file=Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='undo')
        menu.add_cascade(label='Edit', menu=edit)
        return _init_window()

# def main():
#     init_frame(self, master = None)
#     init_window(self)
#
#
# main()
