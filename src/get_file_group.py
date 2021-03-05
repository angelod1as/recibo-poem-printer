import os
import random
from flash_path import flash_path

flash = flash_path()

def find_texts(string):
    return string.endswith(".txt")


def get_file_group(chosen, choice):
    full_dir_list = os.listdir(chosen)
    dir_list = []
    # remove dotfiles
    for dir in full_dir_list:
        if not dir.startswith('.'):
            dir_list.append(dir)
            
    if choice not in ["comics", "kids"]:
        return [file for file in filter(find_texts, dir_list)]

    selected_image_folder = random.choice(dir_list)
    selected_image_path = str(os.path.join(flash, choice, selected_image_folder))
    
    full_image_list = os.listdir(selected_image_path)
    image_dir_list = []
    # remove dotfiles
    for dir in full_image_list:
        if not dir.startswith('.'):
            image_dir_list.append(dir)

    image_group = []
    for image in image_dir_list:
        print('image', image)
        if image.endswith((".jpg", ".JPG")):
            image_path = str(
                os.path.join(flash, choice, selected_image_folder, image)
            )
            image_group.append(image_path)
    return image_group



