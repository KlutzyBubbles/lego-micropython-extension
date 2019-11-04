import pytest
from sys import stdout

from pybricks_ext.tools import (print, wait, StopWatch)

def test_print():
    print(1, sep=' ', end='\n', file=stdout, flush=False)
    print(1, sep=' ', end='\n', file=stdout)
    print(1, sep=' ', end='\n')
    print(1, sep=' ')
    print(1)
    print(1, 2)
    print(1, 2, 3)

def test_wait():
    wait(100)
    with pytest.raises(Exception):
        wait()

class TestStopWatch:

    @pytest.fixture(scope="function")
    def stopwatch(self):
        stopwatch = StopWatch()
        yield stopwatch

    def test_init(self):
        stopwatch = StopWatch()
        with pytest.raises(Exception):
            stopwatch = StopWatch(100)

    def test_time(self, stopwatch):
        stopwatch.time()
        with pytest.raises(Exception):
            stopwatch.time(100)

    def test_pause(self, stopwatch):
        stopwatch.pause()
        with pytest.raises(Exception):
            stopwatch.pause(100)

    def test_resume(self, stopwatch):
        stopwatch.resume()
        with pytest.raises(Exception):
            stopwatch.resume(100)

    def test_reset(self, stopwatch):
        stopwatch.reset()
        with pytest.raises(Exception):
            stopwatch.reset(100)
