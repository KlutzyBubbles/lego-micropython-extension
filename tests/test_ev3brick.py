import pytest
from pybricks_ext import ev3brick as brick
from pybricks_ext.parameters import (SoundFile, ImageFile, Align)

def test_buttons():
    brick.buttons()

def test_light():
    brick.light(None)
    with pytest.raises(Exception):
        brick.light()

def test_sound():
    brick.sound.beep(frequency=500, duration=100, volume=30)
    brick.sound.beep()
    brick.sound.beeps(5)
    brick.sound.file(SoundFile.LEGO, volume=100)
    brick.sound.file(SoundFile.LEGO)
    with pytest.raises(Exception):
        brick.sound.file()
        brick.sound.beeps()

def test_display():
    brick.display.clear()
    brick.display.text("text", coordinate=None)
    brick.display.text("text")
    brick.display.image(ImageFile.EV3, alignment=Align.CENTER, coordinate=None, clear=True)
    brick.display.image(ImageFile.EV3)
    with pytest.raises(Exception):
        brick.display.image()
        brick.display.text()

def test_battery():
    brick.battery.voltage()
    brick.battery.current()
