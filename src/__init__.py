#!/usr/bin/env python3

import pathlib
import random
from get_text_content import get_text_content
from get_file_group import get_file_group

from printer_print import printer_print

import pygame

__version__ = "0.1.0"

print("Starting script")
print("\n")
print("> Press:")
print("> P for POEM")
print("> S for SHORT STORY")
print("> C for COMICS")
print("> Q or ESC quits the program")


pygame.init()
joysticks = []


def print_now(choice):
    file_path = str(pathlib.Path.cwd().joinpath( "files", choice))
    if choice == "comics":
        file_group = get_file_group(file_path, choice)
        printer_print(file_group, "image")
    else:
        file_group = get_file_group(file_path, choice)
        if len(file_group) != 0:
            selected_file = random.choice(file_group)
            selected_path = str(pathlib.Path.cwd().joinpath(file_path, selected_file))
            if selected_file.endswith(".txt"):
                content = get_text_content(selected_path, type=choice)
                printer_print(content, "text")
        else:
            print("Pasta vazia")
            

# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print ("Detected joystick "),joysticks[-1].get_name(),"'"

keepPlaying = True

while keepPlaying:
    for event in pygame.event.get():
        try:
            # the 11 event is keyup
            key_up = event.type == 11
            if key_up:
                key_pressed = event.button
                if key_pressed == 0:
                    print_now("poems")
                elif key_pressed == 1:
                    print_now("short-stories")
                elif key_pressed == 2:
                    print_now("comics")
        except:
            print('An exception ocurred')
