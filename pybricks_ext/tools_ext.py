import sys

from pybricks.tools import StopWatch, print, wait


def print(*value, sep=' ', end='\n', file=sys.stdout, flush=False):
    pybricks.tools.print(value, sep=sep, end=end, file=file, flush=flush)

def wait(time):
    pybricks.tools.wait(time)

class StopWatchExt(StopWatch):

    def __init__(self):
        super(StopWatchExt, self).__init__()

    def wait_until_time_passes(self, time):
        super(StopWatchExt, self).resume()
        while super(StopWatchExt, self).time() < time:
            wait(10)
        return
