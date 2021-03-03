import os
import random
from flash_path import flash_path

flash = flash_path()

def find_texts(string):
    return string.endswith(".txt")


def get_file_group(chosen, choice):
    dir_list = os.listdir(chosen)  # returns list

    if choice not in ["comics", "kids"]:
        return [file for file in filter(find_texts, dir_list)]

    selected_image_folder = random.choice(dir_list)
    selected_image_path = str(os.path.join(flash, choice, selected_image_folder))
    dir_list = os.listdir(selected_image_path)
    image_group = []
    for image in dir_list:
        if image.endswith(".jpg"):
            image_path = str(
                os.path.join(flash, choice, selected_image_folder, image)
            )
            image_group.append(image_path)
    return image_group
