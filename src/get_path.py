import pathlib


def get_path(location):
    thisPath = pathlib.Path.cwd().joinpath("src", "files", location)
    return str(thisPath.absolute())
