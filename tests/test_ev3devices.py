import pytest

from pybricks_ext.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks_ext.parameters import (Port, Stop, Direction)

class TestMotor:

    @pytest.fixture(scope="function")
    def motor(self):
        motor = Motor(Port.A)
        yield motor

    def test_init(self):
        motor = Motor(Port.A, direction=Direction.COUNTERCLOCKWISE, gears=5)
        assert motor.port == Port.A
        assert motor.direction == Direction.COUNTERCLOCKWISE
        assert motor.gears == 5
        motor = Motor(Port.B)
        assert motor.port == Port.B
        assert motor.direction == Direction.CLOCKWISE
        assert motor.gears == None
        with pytest.raises(Exception):
            motor = Motor()

    def test_dc(self, motor):
        motor.dc(100)
        with pytest.raises(Exception):
            motor.dc()

    def test_angle(self, motor):
        motor.angle()
        with pytest.raises(Exception):
            motor.angle(100)

    def test_reset_angle(self, motor):
        motor.reset_angle(100)
        with pytest.raises(Exception):
            motor.reset_angle()

    def test_speed(self, motor):
        motor.speed()
        with pytest.raises(Exception):
            motor.speed(100)

    def test_stop(self, motor):
        motor.stop()
        motor.stop(stop_type=Stop.COAST)
        motor.stop(Stop.COAST)

    def test_run(self, motor):
        motor.run(100)
        with pytest.raises(Exception):
            motor.run()

    def test_run_time(self, motor):
        motor.run_time(100, 1000, stop_type=Stop.COAST, wait=True)
        motor.run_time(100, 1000)
        with pytest.raises(Exception):
            motor.run_time()
        with pytest.raises(Exception):
            motor.run_time(100)
        with pytest.raises(Exception):
            motor.run_time(stop_type=Stop.COAST, wait=True)

    def test_run_angle(self, motor):
        motor.run_angle(100, 1000, stop_type=Stop.COAST, wait=True)
        motor.run_angle(100, 1000)
        with pytest.raises(Exception):
            motor.run_angle()
        with pytest.raises(Exception):
            motor.run_angle(100)
        with pytest.raises(Exception):
            motor.run_angle(stop_type=Stop.COAST, wait=True)

    def test_run_target(self, motor):
        motor.run_target(100, 1000, stop_type=Stop.COAST, wait=True)
        motor.run_target(100, 1000)
        with pytest.raises(Exception):
            motor.run_target()
        with pytest.raises(Exception):
            motor.run_target(100)
        with pytest.raises(Exception):
            motor.run_target(stop_type=Stop.COAST, wait=True)

    def test_track_target(self, motor):
        motor.track_target(100)
        with pytest.raises(Exception):
            motor.track_target()

    def test_stalled(self, motor):
        motor.stalled()
        with pytest.raises(Exception):
            motor.stalled(100)

    def test_run_until_stalled(self, motor):
        motor.run_until_stalled(100, stop_type=Stop.COAST, duty_limit=100)
        motor.run_until_stalled(100)
        with pytest.raises(Exception):
            motor.run_until_stalled()
        with pytest.raises(Exception):
            motor.run_until_stalled(stop_type=Stop.COAST, duty_limit=100)

    def test_set_dc_settings(self, motor):
        motor.set_dc_settings(100, 100)
        with pytest.raises(Exception):
            motor.set_dc_settings()
        with pytest.raises(Exception):
            motor.set_dc_settings(100)

    def test_set_run_settings(self, motor):
        motor.set_run_settings(100, 100)
        with pytest.raises(Exception):
            motor.set_run_settings()
        with pytest.raises(Exception):
            motor.set_run_settings(100)

    def test_set_pid_settings(self, motor):
        motor.set_pid_settings(1, 2, 3, 1000, 360, 90, 90, 1000)
        with pytest.raises(Exception):
            motor.set_pid_settings(1, 2, 3, 1000, 360, 90, 90)
        with pytest.raises(Exception):
            motor.set_pid_settings(1, 2, 3, 1000, 360, 90)
        with pytest.raises(Exception):
            motor.set_pid_settings(1, 2, 3, 1000, 360)
        with pytest.raises(Exception):
            motor.set_pid_settings(1, 2, 3, 1000)
        with pytest.raises(Exception):
            motor.set_pid_settings(1, 2, 3)
        with pytest.raises(Exception):
            motor.set_pid_settings(1, 2)
        with pytest.raises(Exception):
            motor.set_pid_settings(1)
        with pytest.raises(Exception):
            motor.set_pid_settings()

class TestTouchSensor:

    @pytest.fixture(scope='function')
    def sensor(self):
        sensor = TouchSensor(Port.S1)
        yield sensor

    def test_init(self, sensor):
        sensor = TouchSensor(Port.S1)
        assert sensor.port == Port.S1
        with pytest.raises(Exception):
            sensor = TouchSensor()

    def test_pressed(self, sensor):
        sensor.pressed()
        with pytest.raises(Exception):
            sensor.pressed(True)

class TestColorSensor:

    @pytest.fixture(scope='function')
    def sensor(self):
        sensor = ColorSensor(Port.S1)
        yield sensor

    def test_init(self, sensor):
        sensor = ColorSensor(Port.S1)
        assert sensor.port == Port.S1
        with pytest.raises(Exception):
            sensor = ColorSensor()

    def test_color(self, sensor):
        sensor.color()
        with pytest.raises(Exception):
            sensor.color(True)

    def test_ambient(self, sensor):
        sensor.ambient()
        with pytest.raises(Exception):
            sensor.ambient(True)

    def test_reflection(self, sensor):
        sensor.reflection()
        with pytest.raises(Exception):
            sensor.reflection(True)

    def test_rgb(self, sensor):
        sensor.rgb()
        with pytest.raises(Exception):
            sensor.rgb(True)

class TestInfraredSensor:

    @pytest.fixture(scope='function')
    def sensor(self):
        sensor = InfraredSensor(Port.S1)
        yield sensor

    def test_init(self, sensor):
        sensor = InfraredSensor(Port.S1)
        assert sensor.port == Port.S1
        with pytest.raises(Exception):
            sensor = InfraredSensor()

    def test_distance(self, sensor):
        sensor.distance()
        with pytest.raises(Exception):
            sensor.distance(True)

    def test_beacon(self, sensor):
        sensor.beacon(1)
        with pytest.raises(Exception):
            sensor.beacon()

    def test_buttons(self, sensor):
        sensor.buttons(1)
        with pytest.raises(Exception):
            sensor.buttons()

class TestUltrasonicSensor:

    @pytest.fixture(scope='function')
    def sensor(self):
        sensor = UltrasonicSensor(Port.S1)
        yield sensor

    def test_init(self, sensor):
        sensor = UltrasonicSensor(Port.S1)
        assert sensor.port == Port.S1
        with pytest.raises(Exception):
            sensor = UltrasonicSensor()

    def test_distance(self, sensor):
        sensor.distance(silent=False)
        sensor.distance(False)
        sensor.distance()

    def test_presence(self, sensor):
        sensor.presence()
        with pytest.raises(Exception):
            sensor.presence(1)

class TestGyroSensor:

    @pytest.fixture(scope='function')
    def sensor(self):
        sensor = GyroSensor(Port.S1)
        yield sensor

    def test_init(self, sensor):
        sensor = GyroSensor(Port.S1)
        assert sensor.port == Port.S1
        assert sensor.direction == Direction.CLOCKWISE
        sensor = GyroSensor(Port.S2, direction=Direction.COUNTERCLOCKWISE)
        assert sensor.port == Port.S2
        assert sensor.direction == Direction.COUNTERCLOCKWISE
        with pytest.raises(Exception):
            sensor = GyroSensor()

    def test_speed(self, sensor):
        sensor.speed()
        with pytest.raises(Exception):
            sensor.speed(True)

    def test_angle(self, sensor):
        sensor.angle()
        with pytest.raises(Exception):
            sensor.angle(True)

    def test_reset_angle(self, sensor):
        sensor.reset_angle(1)
        with pytest.raises(Exception):
            sensor.reset_angle()
