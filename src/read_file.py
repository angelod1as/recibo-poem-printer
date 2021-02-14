import os
import pathlib
import random


def read_file(chosen):
    dirList = os.listdir(chosen)  # returns list

    def findTexts(string):
        return string.endswith(".txt")

    filtered = []
    for file in filter(findTexts, dirList):
        filtered.append(file)

    randomFile = random.choice(filtered)
    filepath = pathlib.Path.cwd().joinpath(chosen, randomFile)
    return filepath
