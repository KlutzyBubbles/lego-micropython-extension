import sys

from pybricks.tools import StopWatch, print, wait

def print(*value, sep=' ', end='\n', file=sys.stdout, flush=False):
    pybricks.tools.print(value, sep=sep, end=end, file=file, flush=flush)

def wait(time):
    pybricks.tools.wait(time)

class StopWatchExt(StopWatch):
    """
    Extension class for the StopWatch Object
    """

    def __init__(self):
        """
        Initiate the StopWatch Object
        """
        super(StopWatchExt, self).__init__()

    def wait_until_time_passes(self, time):
        """Waits until the time counter passes a specified value.
        If the StopWatch is paused, it will be resumed
        
        :param time: Time value to pass before continuing
        :type time: int
        """
        super(StopWatchExt, self).resume()
        while super(StopWatchExt, self).time() < time:
            wait(10)
        return
