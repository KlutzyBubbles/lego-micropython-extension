Installation
===================

This page guides you through the steps to install the extension methods

What do you need?
-----------------------------------------------------------

To get started, you'll need:

- A Windows 10 or Mac OS computer
- Internet access and administrator access

    This is required during the installation only. You will not need special access to write and run programs later on.

- An EV3 Brick with the EV3 MicroPython OS running
- Visual Studio with the Lego EV3 Extension installed
- A general knowledge of the original MicroPython methods as these extensions are modelled after them

It is recommended to follow the installation guide found `HERE <https://TODO>`_ before continuing.

Connecting to your EV3 brick
-----------------------------------------------------------

To run programs, you should have already connected the brick to the computer but as a refresher, here is how

- Turn the EV3 Brick on
- Connect the EV3 Brick to your computer with the mini-USB cable
- Configure the USB connection as shown in :numref:`fig_connecting`.

.. _fig_connecting:

.. figure:: _images/connecting.png
   :width: 100 %
   :alt: connecting
   :align: center

   Configuring the USB connection between the computer and the EV3 Brick

Installing the Python package
-----------------------------------------------------------

In order to be able to use the extensions functions, the module must be installed onto the brick itself.

1. Right click the brick in the device browser and click SSH
2. Verify the SSH connection by typing fortune
3. Verify pip is installed by typing 'pip -V'

   If pip is not installed, you can install it by running 'python -m pip install --up grade pip'

4. Install the extension by typing 'pip install lego-mp-ext'


Code Linting
-----------------------------------------------------------

We have currently not been able to support true code linting, but we are looking into it
