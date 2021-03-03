PoemPrinter
============================================

*This is a program created in collaboration with Casa1, a LGBTQ+ housing program in Brazil.*

Print from ``.txt`` files into a ``POS-5890C`` Thermal Printer.

.. image:: https://i.imgur.com/17bwnwP.png
  :width: 400
  :alt: Picture of POS-5890C thermal printer with printed poem
  
Before anything
---------------

This is my very first python script. This project is open-source and built for free, but I'd love to be referenced if you fork it/use it anywhere else.

I'd love to see my work being used in other places.

Roadmap
=======

The software development has the following roadmap:

Proof of concept
----------------

1. [DONE] The printer should succesfully print a accented string (``latin-1``) after a program command.

Custom text
-----------

1. [DONE] The program should read from a ``.txt`` file
2. [DONE] The program should format the result from ``read`` accordingly.
3. [DONE] The printer should print succesfully the generated string by the program.

More folders, more texts
------------------------

1. [DONE] The program should read from two folders: ``short-stories`` and ``poems``
2. [DONE] The program should format each file accordingly.
3. [DONE] The printer should print a random text from a single folder after a command.
4. [DONE] The printer should print a random text from a single folder after a key press.

Images
------

1. [DONE] The program should read a ``bitmap`` image.
2. [DONE] The program should format the image accordingly (Maybe here I'll simplify the process by creating mandatory image pre-formatting rules)
3. [DONE] The program should print the image after a command or key press (as it should be already implemented as seen above)
4. [DONE] The program should read, format and print a random image from the ``images`` folder succesfully

Hardware
========

- Raspberry Pi 3 Model B + 16gb card
- POS-5890C printer
- Sandisk 16gb flash drive
- Zero Delay card + nylon arcade buttons

The Zero Delay card, connected to the buttons, feeds controller information through USB to the Raspberry Pi. It, running my program, reads the according file and sends its content to the printer.

**Important**: In order to make the files easily updateable, I did a somewhat hack:

- I have a flash drive connected with a set folder structure
- I edited ``/etc/rc.local`` file at Raspbian like this:

::

    sudo mount /dev/sda1 /mnt
    sudo cp -r /mnt/ /home/pi/poem-printer/files/
    sudo python3 /home/pi/poem-printer/src/__init__.py &

    exit 0

The first line mounts the flash drive, the second copies the files to the local drive and the third starts the script.

The only downside is that it takes a few seconds to boot completely.

(If you know a way to run the script ONLY after the USB drives were mounted succesfully, please let me know. All my attempts failed)

to watch rc.local after boot: ``grep rc.local /var/log/syslog``  

Thanks
======

**First:**

Thanks to `Casa 1 <https://www.casaum.org/>`_. They financed this project through buying the necessary hardware.

If you have money to spare, consider donating to them. They are a home for LGBTQ+ people that were denied housing and rights.

**Second:**

This thing only works because of the amazing help from `Belono <https://github.com/belono>`_ and the `Python ESC/POS <https://github.com/python-escpos/python-escpos/>`_ contributors.

Many thanks to `Cuducos <https://github.com/cuducos>`_ for Python tools and clarification on some doubts. Thanks to `Jonas Marques <https://twitter.com/jonassmarques>`_ for his tips and answers to my many (many!) questions.

PRs are encouraged and appreciated.
