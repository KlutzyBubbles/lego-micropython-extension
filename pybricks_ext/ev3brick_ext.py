import _thread
from pybricks import ev3brick as brick

class SpeakerExt():

    def beep(frequency=500, duration=100, volume=30, wait=False):
        if wait:
            brick.sound.beep(frequency=frequency, duration=duration, volume=volume)
        else:
            _thread.start_new_thread(brick.sound.beep, (), {"frequency": frequency, "duration": duration, "volume": volume})

    def beeps(number, wait=False):
        if wait:
            brick.sound.beeps(number)
        else:
            _thread.start_new_thread(brick.sound.beeps, (number))

    def file(file_name, volume=100, wait=False):
        if wait:
            brick.sound.file(file_name, volume=volume)
        else:
            _thread.start_new_thread(brick.sound.file, (file_name), {"volume": volume})

flashing_lock = _thread.allocate_lock()

def light_pulse(color, short_pause=200, long_pause=800, on_pause=100):
    _thread.start_new_thread(_true_light_pulse, (color, short_pause, long_pause, on_pause))

def _true_light_pulse(color, short_pause, long_pause, on_pause):
    if not flashing_lock.acquire():
        return
    while True:
        brick.light(color)
        wait(on_pause)
        brick.light(None)
        wait(short_pause)
        brick.light(color)
        wait(on_pause)
        brick.light(None)
        wait(long_pause)

def light_flash(color, off_pause=500, on_pause=500):
    _thread.start_new_thread(_true_light_flash, (color, off_pause, on_pause))

def _true_light_flash(color, off_pause, on_pause):
    if not flashing_lock.acquire():
        return
    while True:
        brick.light(color)
        wait(on_pause)
        brick.light(None)
        wait(off_pause)