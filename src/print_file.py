from printer import print_string
from textwrap import fill

characterLimit = 32  # characters per line

# "./src/files/test.txt"


def print_file(filepath):
    file = open(filepath)
    content = file.read()
    paragraphList = content.split("\n")

    def wrapText(string):
        return fill(string, characterLimit)

    mappedList = [*map(wrapText, paragraphList)]
    result = "\n".join(mappedList)

    print(result)
    print_string(result)
