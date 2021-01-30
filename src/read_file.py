import os
import random
from print_file import print_file


def read_file(chosen):
    list = os.listdir(chosen)  # returns list

    def findTexts(string):
        try:
            string.index(".txt")
            return True
        except ValueError:
            return False

    def formatPath(folder, file):
        if folder[-1] != "/":
            folder = folder + "/"
        return folder + file

    filtered = [*filter(findTexts, list)]
    randomFile = random.choice(filtered)
    filepath = formatPath(chosen, randomFile)

    print_file(filepath)
