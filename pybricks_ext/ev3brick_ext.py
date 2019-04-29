import threading

from pybricks import ev3brick as brick
from pybricks.parameters import Color
from pybricks.tools import wait

import _thread

flashing_lock = None

def light_pulse(color, short_pause=200, long_pause=800, on_pause=100):
    """Set the brick light to pulse a color
    
    :param color: Color of the light
    :type color: ColorExt
    :param short_pause: Duration of the short pause, defaults to 200
    :type short_pause: int, optional
    :param long_pause: Duration of the long pause, defaults to 800
    :type long_pause: int, optional
    :param on_pause: Duration of the light flashing on, defaults to 100
    :type on_pause: int, optional
    """
    global flashing_lock
    if isinstance(flashing_lock, LightPulse):
        flashing_lock.kill()
        flashing_lock = None
    if color is None or ColorExt.compare(color, Color.BLACK):
        light(None)
    else:
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
    """Set the brick light to flash a color
    
    :param color: Color of the light
    :type color: Color
    :param off_pause: Duration of the off pause, defaults to 500
    :type off_pause: int, optional
    :param on_pause: Duration of the on puase, defaults to 500
    :type on_pause: int, optional
    """
    global flashing_lock
    if isinstance(flashing_lock, LightPulse):
        flashing_lock.kill()
        flashing_lock = None
    flashing_lock = LightFlash(color, off_pause, on_pause)
    flashing_lock.start()

def light(color):
    global flashing_lock
    if isinstance(flashing_lock, (LightPulse, LightFlash)):
        flashing_lock.kill()
        flashing_lock = None
    brick.light(color)

def buttons():
    return brick.buttons()

class SpeakerExt():
    """
    Extension class for the Speaker Object
    """

    def beep(frequency=500, duration=100, volume=30, wait=False):
        """Play a beep/tone
        
        :param frequency: Frequency of the beep, defaults to 500
        :type frequency: int, optional
        :param duration: Duration of the beep, defaults to 100
        :type duration: int, optional
        :param volume: Volume of the beep, defaults to 30
        :type volume: int, optional
        :param wait: Whether to wait for the beep to finish before continuing, defaults to False
        :type wait: bool, optional
        """
        if wait:
            brick.sound.beep(frequency=frequency, duration=duration, volume=volume)
        else:
            threading.Thread(target=brick.sound.beep, kwargs={"frequency": frequency, "duration": duration, "volume": volume})

    def beeps(number, wait=False):
        """Play a number of default beeps with a brief pause in between
        
        :param number: Number of beeps
        :type number: int
        :param wait: Whether to wait for the beeps to finish before continuing, defaults to False
        :type wait: bool, optional
        """
        if wait:
            brick.sound.beeps(number)
        else:
            threading.Thread(target=brick.sound.beeps, args=(number))

    def file(file_name, volume=100, wait=False):
        """Play a sound file
        
        :param file_name: Path to the sound file, including extension
        :type file_name: SoundFile, str
        :param volume: Volume of the sound, defaults to 100
        :type volume: int, optional
        :param wait: Whether to wait for the sound to finish before continuing, defaults to False
        :type wait: bool, optional
        """
        if wait:
            brick.sound.file(file_name, volume=volume)
        else:
            threading.Thread(target=brick.sound.file, args=(file_name), kwargs={"volume": volume})

sound = SpeakerExt()
display = brick.display
battery = brick.battery