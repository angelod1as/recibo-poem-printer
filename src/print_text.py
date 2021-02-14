# printer.py
import pathlib
from escpos.printer import Usb
from get_content import get_content

from get_path import get_path

# 32 characters per line
p = Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)
p.charcode("CP860")

headerPath = pathlib.Path.cwd().joinpath(get_path("information"), "header.txt")
header = get_content(headerPath)

footerPath = pathlib.Path.cwd().joinpath(get_path("information"), "footer.txt")
footer = get_content(footerPath)

spacing = "\n\n"


def print_text(string):
    p.text(header)
    p.text(spacing)
    p.text(string)
    p.text(spacing)
    p.text(footer)
    p.cut()
