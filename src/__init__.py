from read_file import read_file
from get_keypress import get_keypress

__version__ = "0.1.0"

poems = "./src/files/poems"
short_stories = "./src/files/short-stories"

print("Starting script")
print("\n> Press:\n> P for POEM\n> S for SHORT STORY")

key = ""

while key != "'\\x1b'":
    key = get_keypress()
    if key == "'p'":
        read_file(poems)
    elif key == "'s'":
        read_file(short_stories)
