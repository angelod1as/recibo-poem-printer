import pathlib
import random
from get_content import get_content
from get_file_group import get_file_group

from get_keypress import get_keypress
from get_path import get_path

__version__ = "0.1.0"


print("Starting script")
print("\n")
print("> Press:")
print("> P for POEM")
print("> S for SHORT STORY")
print("> C for COMICS")
print("> Q or ESC quits the program")


key = ""


def print_now(choice):
    file_path = get_path(choice)
    file_group = get_file_group(file_path)
    if len(file_group) != 0:
        selected_text = random.choice(file_group)
        text_path = pathlib.Path.cwd().joinpath(file_path, selected_text)
        content = get_content(text_path)
        print(content)
    else:
        print("Pasta vazia")


while key not in ["'q'", "'\\x1b'"]:
    key = get_keypress()
    if key == "'p'":
        print_now("poems")

    elif key == "'s'":
        print_now("short-stories")

    elif key == "'c'":
        print_now("comics")
