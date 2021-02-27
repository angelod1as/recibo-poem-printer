# printer.py
import os
import pathlib
from escpos.printer import Usb
from get_text_content import get_text_content
from flash_path import flash_path

# 32 characters per line
p = Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)
p.charcode('PORTUGUESE')

headerPath = str(os.path.join(flash_path, "information", "header.txt"))
header = get_text_content(headerPath)

footerPath = str(os.path.join(flash_path, "information", "footer.txt"))
footer = get_text_content(footerPath)

spacing = "\n\n"


def printer_print(content, type):
    p.text(header)
    p.text(spacing)
    if type == "text":
        p.text(content)
    if type == "image":
        for image in content:
            p.image(image, fragment_height=500)
    p.text(spacing)
    p.text(footer)
    p.cut()
