import threading

from pybricks import ev3brick as brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

import _thread

flashing_lock = None
sound = SpeakerExt()
display = brick.display
battery = brick.battery

def light_pulse(color, short_pause=200, long_pause=800, on_pause=100):
    global flashing_lock
    if isinstance(flashing_lock, LightPulse):
        flashing_lock.kill()
    flashing_lock = LightPulse(color, short_pause, long_pause, on_pause)
    flashing_lock.start()


class LightPulse(threading.Thread):

    def __init__(self, color, short_pause, long_pause, on_pause):
        super(LightPulse, self).__init__()
        self.color = color
        self.short_pause = short_pause
        self.long_pause = long_pause
        self.on_pause = on_pause
        self.stop = False

    def run(self):
        while not self.stop:
            brick.light(self.color)
            wait(self.on_pause)
            if self.stop:
                return
            brick.light(None)
            wait(self.short_pause)
            if self.stop:
                return
            brick.light(self.color)
            wait(self.on_pause)
            if self.stop:
                return
            brick.light(None)
            wait(self.long_pause)

    def kill(self):
        self.stop = True

class LightFlash(threading.Thread):

    def __init__(self, color, off_pause, on_pause):
        super(LightPulse, self).__init__()
        self.color = color
        self.off_pause = off_pause
        self.on_pause = on_pause
        self.stop = False

    def run(self):
        while not self.stop:
            brick.light(self.color)
            wait(self.on_pause)
            if self.stop:
                return
            brick.light(None)
            wait(self.off_pause)

    def kill(self):
        self.stop = True

def light_flash(color, off_pause=500, on_pause=500):
    global flashing_lock
    if isinstance(flashing_lock, LightPulse):
        flashing_lock.kill()
    flashing_lock = LightFlash(color, off_pause, on_pause)
    flashing_lock.start()

def light(color):
    brick.light(color)

class SpeakerExt():

    def beep(frequency=500, duration=100, volume=30, wait=False):
        if wait:
            brick.sound.beep(frequency=frequency, duration=duration, volume=volume)
        else:
            threading.Thread(target=brick.sound.beep, kwargs={"frequency": frequency, "duration": duration, "volume": volume})

    def beeps(number, wait=False):
        if wait:
            brick.sound.beeps(number)
        else:
            threading.Thread(target=brick.sound.beeps, args=(number))

    def file(file_name, volume=100, wait=False):
        if wait:
            brick.sound.file(file_name, volume=volume)
        else:
            threading.Thread(target=brick.sound.file, args=(file_name), kwargs={"volume": volume})
