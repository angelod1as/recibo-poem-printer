#!/usr/bin/env python3

__version__ = "1.0.0"

import sys
import os
import random
from flash_path import flash_path
from get_text_content import get_text_content
from get_file_group import get_file_group

from printer_print import printer_print

import pygame

print("Printer program started")

pygame.init()
joysticks = []
ip = "null"
if len(sys.argv) > 1:
    ip = str(sys.argv[1])

def print_now(choice):
    flash = flash_path()
    if flash:
        file_path = str(os.path.join(flash, choice))
        if choice in ["comics", "kids"]:
            file_group = get_file_group(file_path, choice)
            printer_print(file_group, "image", file_group)
        else:
            file_group = get_file_group(file_path, choice)
            if len(file_group) != 0:
                selected_file = random.choice(file_group)
                selected_path = str(os.path.join(file_path, selected_file))
                if selected_file.endswith(".txt"):
                    content = get_text_content(selected_path, type=choice)
                    printer_print(content, "text", selected_path)
            else:
                print("Pasta vazia")
    else:
        print("MEDIA NOT FOUND")

printer_print(ip, "start", "")

# for al the connected joysticks
for i in range(pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    print("Detected joystick "), joysticks[-1].get_name(), "'"

keepPlaying = True

while keepPlaying:
    for event in pygame.event.get():
        key_up = event.type == 11
        if event.type == 7:
            print("Poem Printer script aborted")
            sys.exit("Poem Printer script aborted")
        if key_up:
            key_pressed = event.button
            if key_pressed == 0:
                print_now("poems")
            elif key_pressed == 1:
                print_now("short-stories")
            elif key_pressed == 2:
                print_now("comics")
            elif key_pressed == 3:
                print_now("kids")
