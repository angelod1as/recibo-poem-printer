from curtsies import Input


def get_keypress():
    with Input(keynames="curses") as input_generator:
        for e in input_generator:
            return repr(e)
