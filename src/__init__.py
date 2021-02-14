import pathlib
import random
from get_text_content import get_text_content
from get_file_group import get_file_group

from get_keypress import get_keypress
from printer_print import printer_print

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
    file_path = str(pathlib.Path.cwd().joinpath("src", "files", choice))
    if choice == "comics":
        file_group = get_file_group(file_path, choice)
        printer_print(file_group, "image")
    else:
        file_group = get_file_group(file_path, choice)
        if len(file_group) != 0:
            selected_file = random.choice(file_group)
            selected_path = str(pathlib.Path.cwd().joinpath(file_path, selected_file))
            if selected_file.endswith(".txt"):
                content = get_text_content(selected_path)
                printer_print(content, "text")
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
