from PIL import Image
from . import Pathing


def resize(dir_path, destination, img_size, sub_path, file):
    im = Image.open(dir_path + file)
    title = Pathing.remove_extension(file)
    img_resize = im.resize((img_size, img_size), Image.ANTIALIAS)
    img_resize.save(destination + title + sub_path + ".png", 'PNG', quality=95)


