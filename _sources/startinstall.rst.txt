Installation
===================

This page guides you through the steps to install the extension methods

What do you need?
-----------------------------------------------------------

To get started, you'll need:

- A Windows 10 or Mac OS computer
- Internet access and administrator access

    This is required during the installation only. You will not need special
    access to write and run programs later on.

- An EV3 Brick with the EV3 MicroPython OS running
- Visual Studio with the Lego EV3 Extension installed
- A general knowledge of the original MicroPython methods as these extensions
    are modelled after them

It is recommended to follow the installation guide found `HERE <https://klutzybubbles.github.io/lego-micropython-skeleton/startinstall.html>`_ before continuing.

Connecting to your EV3 brick
-----------------------------------------------------------

To run programs, you should have already connected the brick to the computer
but as a refresher, here is how

- Turn the EV3 Brick on
- Connect the EV3 Brick to your computer with the mini-USB cable
- Configure the USB connection as shown in :numref:`fig_connecting`.

.. _fig_connecting:

.. figure:: images/connecting.png
   :width: 100 %
   :alt: connecting
   :align: center

   Configuring the USB connection between the computer and the EV3 Brick

Installing the Python package
-----------------------------------------------------------

Unfortunately due to the minimalistic nature of upip and pybricks-MicroPython
the package does not currently support being installed globally on the brick
itself instead it must be installed into each project by typing
:mod:`pip install -t . --upgrade lego-mp-extension`

Code Linting
-----------------------------------------------------------

The extension methods within the module have full code linting functionalities,
but only parts of the core methods are linted within the exten sion, to add the
missing methods just install 'lego-mp-skeleton' to the development environment.

Do NOT install the skeleton to:
    - The brick itself
    - The bricks program folder
    - Any machine the brick can run code from

Doing this will cause the brick methods to potentially be overriden and
severly affect the bricks performance or prevent any program from running on
the brick.

use :mod:`pip install [--user] --upgrade lego-mp-skeleton` to install the
skeleton with the [] being optional
