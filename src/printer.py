# printer.py
from escpos.printer import Usb

# 32 characters per line
p = Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)
p.charcode("CP860")


def print_string(string):
    print(string)
    # p.text("\n")
    # p.text(string)
    # p.cut()
