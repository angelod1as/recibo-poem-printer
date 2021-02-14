import pathlib
from print_file import print_file
from read_file import read_file

from get_keypress import get_keypress

__version__ = "0.1.0"


def getPath(location):
    thisPath = pathlib.Path.cwd().joinpath("src", "files", location)
    return thisPath.absolute()


poems = str(getPath("poems"))
short_stories = str(getPath("short-stories"))
images = str(getPath("images"))


print("Starting script")
print("\n")
print("> Press:")
print("> P for POEM")
print("> S for SHORT STORY")
print("> Q or ESC quits the program")


key = ""


while key not in ["'q'", "'\\x1b'"]:
    key = get_keypress()
    if key == "'p'":
        filepath = read_file(getPath("poems"))
        print_file(filepath)

    elif key == "'s'":
        filepath = read_file(getPath("short-stories"))
        print_file(filepath)
