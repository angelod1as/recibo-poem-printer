# printer.py
from escpos.printer import Usb

# from get_path import getPath

# from print_file import print_file
# from read_file import read_file

# 32 characters per line
p = Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)
p.charcode("CP860")

# header = read_file(str(getPath("poems")))
# print(header)


def print_string(string):
    print(string)
    # p.text("\n")
    # p.text(string)
    # p.cut()
