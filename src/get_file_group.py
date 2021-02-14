import os


def get_file_group(chosen):
    dirList = os.listdir(chosen)  # returns list

    def findTexts(string):
        return string.endswith(".txt")

    filtered = []
    for file in filter(findTexts, dirList):
        filtered.append(file)

    return filtered
