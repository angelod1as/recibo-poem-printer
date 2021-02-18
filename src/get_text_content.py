from textwrap import fill

character_limit = 32  # characters per line


def get_text_content(filepath, type="text"):
    file = open(filepath)
    content = file.read()
    paragraph_list = content.split("\n")

    def wrapText(string):
        if type == "poems":
            return fill(string, width=character_limit - 2, subsequent_indent="/ ")
        else:
            return fill(string, width=character_limit)

    mapped_list = []
    for text in map(wrapText, paragraph_list):
        mapped_list.append(text)

    result = "\n".join(mapped_list)

    return result
