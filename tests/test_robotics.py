import pytest

from pybricks_ext.robotics import DriveBase
from pybricks_ext.parameters import (Port, Stop)

class TestMotor:

    @pytest.fixture(scope="function")
    def drive_base(self):
        drive_base = DriveBase(Port.A, Port.B, 100, 200)
        yield drive_base

    def test_init(self):
        drive_base = DriveBase(Port.A, Port.B, 100, 200)
        assert drive_base.left_motor == Port.A
        assert drive_base.right_motor == Port.B
        assert drive_base.wheel_diameter == 100
        assert drive_base.axle_track == 200
        with pytest.raises(Exception):
            drive_base = DriveBase(Port.A, Port.B, 100)
        with pytest.raises(Exception):
            drive_base = DriveBase(Port.A, Port.B)
        with pytest.raises(Exception):
            drive_base = DriveBase(Port.A)
        with pytest.raises(Exception):
            drive_base = DriveBase()

    def test_drive(self, drive_base):
        drive_base.drive(100, 200)
        with pytest.raises(Exception):
            drive_base.drive(100)
        with pytest.raises(Exception):
            drive_base.drive()

    def test_drive_time(self, drive_base):
        drive_base.drive_time(100, 200, 300)
        with pytest.raises(Exception):
            drive_base.drive_time(100, 200)
        with pytest.raises(Exception):
            drive_base.drive_time(100)
        with pytest.raises(Exception):
            drive_base.drive_time()

    def test_stop(self, drive_base):
        drive_base.stop(stop_type=Stop.COAST)
        drive_base.stop()
