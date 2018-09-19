import os
import imageio

img_dir = 'game_background'
images = []
for file_name in os.listdir(img_dir):
    if file_name.endswith( '.jpg'):
        file_path = os.path.join(img_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('game_background/kakuna.gif', images)
images.pop()


# background = .open_file_as_pil_image('game_background/kakuna.gif')
