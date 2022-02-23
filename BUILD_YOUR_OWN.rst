Recibo, the Poem Printer
============================================

Build your own
==============

- Raspberry Pi 3 Model B + 16gb card
- POS-5890C printer
- Sandisk 16gb flash drive
- Zero Delay card + nylon arcade buttons

The Zero Delay card, connected to the buttons, feeds controller information through USB to the Raspberry Pi. It, running my program, reads the according file and sends its content to the printer.

Flash drive
-----------

You must have, inside the flash drive, the following file structure:

- a ``DO_NOT_DELETE.txt`` empty file
- a ``poem-printer`` folder with this script
- a ``files`` folder with your text/images folders
  - The working version has four folders: comics, poems, short-stories and kids.
  - In order to add more folders, you need to edit the code in ``__init__.py``.


Zero Delay card
---------------

The Zero Delay card is self-configurable. The only necessary part is knowing which button triggers each event.

Sadly, this can only be done by trial-and-error (connect a button, press it, see if anything happens, note it down) or by changing the code in ``__init__.py`` that receives the button inputs (around the end of the file).

Raspberry Pi
------------

It's easier to flash an existing Poem Printer card, but if not found, you need to do the following manually to a fresh Raspbian install.

Copy the ``flash_drive.sh`` to your Raspbian home folder, then edit ``/etc/rc.local`` file at Raspbian like this:

::

    # Mounts the flash drive and copies the files to your Pi
    sudo sh /home/flash_drive.sh
    # Runs the script
    sudo python3 /home/pi/poem-printer/poem-printer/src/__init__.py &

    exit 0

- The ``/dev/sda1`` can change, depending on your system.

The only downside is that it takes a few seconds to boot completely.

(If you know a way to run the script ONLY after the USB drives were mounted succesfully, please let me know. All my attempts failed)

to watch rc.local after boot: ``grep rc.local /var/log/syslog``

To test without rebooting, run ``sude /etc/rc.local`` on your Pi. If it complains about ``resource busy``, restart your printer.

There is a ``kill button`` implemented in this version. It's a button that, when clicked, quits the process and allows you to restart it.