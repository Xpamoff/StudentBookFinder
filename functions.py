from datetime import datetime
from PIL import Image


def time_definer():
    time = str(datetime.now())
    time = "_".join(time.split(" "))
    time = "".join(time.split(":"))
    return time


def show_image(file_path):
    im = Image.open(file_path)
    im.show()
