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

At this moment, the software is at it's 80% mark. I need to find out how to make a custom hardware to send commands to it and understand how to run this without hitches and errors.

I'm thinking Raspberry Pi. I have *never* even seen one of those in my life. This will be a nice journey.

Thanks
======

This thing only works because of the amazing help from `Belono <https://github.com/belono>`_ and the `Python ESC/POS <https://github.com/python-escpos/python-escpos/>`_ contributors.

Many thanks to `Cuducos <https://github.com/cuducos>`_ for Python tools and clarification on some doubts.

PRs are encouraged and appreciated.
