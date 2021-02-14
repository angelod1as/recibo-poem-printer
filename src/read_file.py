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

    if len(filtered) != 0:
        randomFile = random.choice(filtered)
        filepath = pathlib.Path.cwd().joinpath(chosen, randomFile)
        print(filepath)
        return filepath
    else:
        print("Pasta vazia")
        return False
