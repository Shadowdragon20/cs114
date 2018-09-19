import os
import makegif
import imageio
from tkinter import *
from PIL import Image

class Window(Frame):
    def _init_(self, master=None):
        Frame._init_(self, master)
        self.master = master
        self.init_window()

    # def background():
    #     img_dir = 'game_gif'
    #
    #     images = []
    #
    #     for file_name in os.listdir(img_dir):
    #         if file_name.endswith('.jpg'):
    #             file_path = os.path.join(img_dir, file_name)
    #             images.append(imageio.imread(file_path))
    #     imageio.mimsave('game_gif/kakuna.gif', images)

    # def showImg():
    #     images = background
    #     background = ['']






    # def resize_pil_image(image):
    #     img.place(x=0,y=0)
    # #
    # def run_animation():
    #
    #     while True:
    #         try:
    #             global photo
    #             global frame
    #             global label
    #             photo = Photoimage(
    #                 file = photo_path,
    #                 format = 'gif - [game_background/glitch0.jpg/glicth1.jpg]'.format(frame)
    #         )
    #need to fix this file path > [game_background/glitch0.jpg/glicth1.jpg]
    #             label.configure(image = nextframe)
    #
    #             frame = frame + 1
    #
    #         except Exception:
    #             frame = 1
    #             break





    #def open_file_as_pil_image(source_file):
       #"""Return a new Image object from source file."""
      # return Image.open(source_file)


    #def _repr_(self):
        #return 'Window(Frame)({!r},{!r},{!r})'.format(
        #im= open_file_as_pil_image('imgholder.png')


        # )


    # def init_window(self):
    #     self.pack(fill=BOTH, expand=1)
    #
    #     quitButton = Button(self, text="Quit")
    #     quitButton.place(x=0, y=0)
    #
    #
    #     quitbutton.pack()
    #
    #
    #     def closewindow():
    #         exit()
    #
    #         button= Button(master, text='Quit')
    #         button.pack()
    #         mainloop()

    # class Image:
    #     image = []
    #     for filename in filenames:
root =Tk()

root.title('One Glitch Game')
#
# picture = PhotoImage.o('game_gif/kakuna.gif')

photo_path = ('game_background/kakuna.gif')
photo = PhotoImage(
    file = photo_path
)
label=Label(
    image = photo
)
# animate = Button(
#     root,
#     text = "animate",
#     command = run_animation()
#     )
label.pack()
# animate.pack()
root.geometry("1000x800")

app = Window(root)
root.mainloop()
