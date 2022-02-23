# printer.py
import os
from escpos.printer import Usb
from get_text_content import get_text_content
from flash_path import flash_path

# 32 characters per line
p = Usb(0x0416, 0x5011, in_ep=0x81, out_ep=0x03)
p.charcode("PORTUGUESE")

flash = flash_path()
if flash:
    headerPath = str(os.path.join(flash, "information", "header.txt"))
    header = get_text_content(headerPath)

    footerPath = str(os.path.join(flash, "information", "footer.txt"))
    footer = get_text_content(footerPath)

    spacing = "\n\n"

    def printer_print(content, type, file_path):
        p.text(header)
        p.text(spacing)
        if type == "start":
            try:
                print(content)
                p.text("Iniciando RECIBO\nUm projeto com código de\nAngelo Dias\nwww.angelodias.com.br\n\n")

                if content ==  "null":
                    p.text("Não estou conectado a internet, não tenho IP")
                else:
                    p.text("Meu endereço IP é: ")
                    p.text(content)
            except UnicodeEncodeError as e:
                p.text("Oops, há algo errado com a impressora/usb/computador")                
        if type == "text":
            try:
                p.text(content)
            except UnicodeEncodeError as e:
                print(file_path)
                print(str(e))
                p.text("Tem coisas da gente que não são defeito nem erro: são só jeito da gente ser. (Caio F. Abreu)\n\nDesta vez, o erro foi aqui:\n")
                p.text(file_path)
                p.text("\n")
                p.text(str(e))
        if type == "image":
            for image in content:
                p.image(image, fragment_height=300)
        p.text(spacing)
        p.text(footer)
        p.cut()


else:
    print("USB Flash Drive not found")
