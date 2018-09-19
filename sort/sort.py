"""Throwaway program to demonstrate color spaces and mapping 2D."""

from PIL import Image
import random

def open_file_as_pil_image(source_file):
    """Return a new Image object from source file."""
    return Image.open(source_file)


def create_empty_pil_image(pil_image):
    """Create an empty PIL Image."""
    return Image.new('RGB', (pil_image.size[0], pil_image.size[1]))


def resize_pil_image(image):
    """Resize PIL image object, fixing largest dimension to 1080px."""
    width = image.size[0]
    height = image.size[1]
    ratio = width / height
    if ratio >= 1:
        width = 810
        height = int(width / ratio)
    else:
        height = 810
        width = int(height * ratio)
    return image.resize((width, height))


def refactor_and_sort_data(color_data):
    """Covert RGB three-tuple and sort newly converted HLS data."""
    return sorted(color_data)


def rgb_shift(seed_num):
    seed_num += 100
    if seed_num > 255:
        seed_num -= 256
    return seed_num


def rand_shift(seed_num, seed_rand):
    seed_num += seed_rand
    if seed_num > 255:
        seed_num -= 256
    return seed_num


def actual_pixel_sort(color_data):
    """some kind of actual pixel sorting to make art or at least try"""
    color_data = [tuple(rgb_shift(i) for i in toop) for toop in color_data]
    return color_data


def random_pixel_sort(color_data):
    """some kind of actual pixel sorting to make art or at least try"""
    rand_num = random.randint(0, 255)
    # rand_num2 = random.randint(0, 255)
    # rand_num3 = random.randint(0, 255)
    color_data = [tuple(rand_shift(i, rand_num) for i in toop) for toop in color_data]
    print(color_data[:2])
    # color_data = [tuple(rand_shift(a, rand_num), rand_shift(b, rand_num2), rand_shift(c, rand_num3) for a,b,c in toop) for toop in color_data]
    # color_data = [tuple((10, 125, 250) for (a, b, c) in toop) for toop in color_data]
    print(rand_num)
    return color_data


def main():
    """."""
    # im = open_file_as_pil_image('test_imgs/leonardo_mona_lisa.jpg')
    im = open_file_as_pil_image('Lucifer.jpg')

    width, height = im.size[0], im.size[1]

    if width > 1080 or height > 1080:
        im = resize_pil_image(im)

    rgb_data = im.getdata()
    sorted_hls_data = refactor_and_sort_data(rgb_data)
    # shifted_rgb_data = actual_pixel_sort(rgb_data)
    print(type(rgb_data))
    print(type(sorted_hls_data))
    print("sorted_hls_data")
    print(sorted_hls_data[:2])
    randshifted_rgb_data = random_pixel_sort(rgb_data)
# new code here
    new_transform = sorted_hls_data

    # for rgb_tup in sorted_hls_data

    print(new_transform[:2])
    # sorted_im = create_empty_pil_image(im)
    # sorted_im.putdata(sorted_hls_data)
    #
    # shifted_im = create_empty_pil_image(im)
    # shifted_im.putdata(shifted_rgb_data)

    randshift_im = create_empty_pil_image(im)
    randshift_im.putdata(randshifted_rgb_data)

    # sorted_im.save('../wip/3Dsort/rgb_mona_lisa.png')
    # sorted_im.save('../../img/test11_out.png')
    # shifted_im.save('../../img/test04s_out.png')

    # for x in range(1, 10):
    #     randshift_im.save('../../img/test16_out' + str(x) + '.png')

    randshift_im.save('Lucifer.jpg')
    print("\U0001f47e" + " enjoy pixel sort " + "\U0001f47e")


if __name__ == '__main__':
    main()
