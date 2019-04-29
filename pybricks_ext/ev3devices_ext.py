from operator import eq, ge, gt, le, lt, ne

from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                 Motor, TouchSensor, UltrasonicSensor)
from pybricks.parameters import Stop
from pybricks.tools import wait, StopWatch

from parameters_ext import ColorExt
from speed_util import get_ratio, speed_deg

def _operator_calc(val_a, val_b, operator):
    operators = {'>': gt,
                 '<': lt,
                 '>=': ge,
                 '<=': le,
                 '==': eq,
                 '!=': ne}
    return operators[operator](val_a, val_b)

class MotorExt(Motor):
    """
    Extension class for the Motor device with useful functions
    mainly relating to speed and specific gear targeting

    Further documentation for the Motor class can be found
    'https://klutzybubbles.github.io/lego-micropython-docs/ev3devices.html#ev3devices.Motor'

    :param port: Port to which motor is connected
    :type port: Port
    :param direction: Direction of the positive motor speed, defaults to Direction.CLOCKWISE
    :type direction: Direction, optional
    :param gears: List of gears linked to the motor, defaults to None
    :type gears: list, tuple, optional
    """

    def output_angle(self, depth=None):
        """
        Get the rotation angle of the motor or its linked gears

        :param depth: Depth of the gear in the link to get the angle for, defaults to None
        :type depth: int, optional

        :return: Motor angle
        :rttype: int, float
        """
        return super(MotorExt, self).angle() * get_ratio(self.gears, depth=depth)

    def output_speed(self, depth=None):
        """
        Gets the speed (angular velocity) of the motor or its linked gears

        :param depth: Depth of the gear in the link to get the angle for, defaults to None
        :type depth: int, optional
        :return: Rotational speed in deg/s
        :rtype: int, float
        """
        return super(MotorExt, self).speed() * get_ratio(self.gears, depth=depth)

    def output_run(self, speed, depth=None):
        """
        Keep the motor or linked gears running at a constant speed (angular velocity)

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            super(MotorExt, self).run(speed)
        super(MotorExt, self).run(speed / get_ratio(self.gears, depth=depth))

    def output_percent_run(self, speed, rpm=240, depth=None):
        """Keep the motor or linked gears running at a constant speed (percentage)

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param rpm: RPM of the Motor, defaults to 240
        :type rpm: int, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            self.percent_run(speed, rpm=rpm)
        super(MotorExt, self).run(speed_deg(speed, rpm=rpm) / get_ratio(self.gears, depth=depth))

    def percent_run(self, speed, rpm=240):
        """Keep the motor running at a constant speed (percentage)

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor
        :type speed: int, float
        :param rpm: RPM of the Motor, defaults to 240
        :type rpm: int, optional
        """
        super(MotorExt, self).run(speed_deg(speed, rpm=rpm))

    def output_run_time(self, speed, time, stop_type=Stop.COAST, wait=True, depth=None):
        """Keep the motor or linked gears running at a constant speed for a
        specified amount of time

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param time: Duration (milliseconds) of the maneuver
        :type time: int
        :param stop_type: Whether to coast, brake or hold after coming to a stand still,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            super(MotorExt, self).run_time(speed, time, stop_type=stop_type, wait=wait)
        super(MotorExt, self).run_time(speed / get_ratio(self.gears, depth=depth),
                                       time,
                                       stop_type=stop_type,
                                       wait=wait)

    def output_percent_run_time(self, speed, time, stop_type=Stop.COAST, wait=True,
                                rpm=240, depth=None):
        """Keep the motor or linked gears running at a constant speed (percentage)
        for a specified amount of time

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear (percentage)
        :type speed: int, float
        :param time: Duration (milliseconds) of the maneuver
        :type time: int
        :param stop_type: Whether to coast, brake or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            self.percent_run_time(speed, time, stop_type=stop_type, wait=wait, rpm=rpm)
        super(MotorExt, self).run_time(
            speed_deg(speed, rpm=rpm) / get_ratio(self.gears, depth=depth),
            time, stop_type=stop_type, wait=wait)

    def percent_run_time(self, speed, time, stop_type=Stop.COAST, wait=True, rpm=240):
        """Keep the motor running at a constant speed (percentage) for a speicified amount of time

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear (percentage)
        :type speed: int, float
        :param time: Duration (milliseconds) of the maneuver
        :type time: int
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        """
        super(MotorExt, self).run_time(speed_deg(speed, rpm=rpm),
                                       time, stop_type=stop_type, wait=wait)

    def output_run_angle(self, speed, rotation_angle, stop_type=Stop.COAST, wait=True, depth=None):
        """Keep the motor or linked gears running at a constant speed for a
        speicified amount of degrees

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param rotation_angle: Angle (degrees) by which the Motor should run
        :type rotation_angle: int
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            super(MotorExt, self).run_angle(speed, rotation_angle, stop_type=stop_type, wait=wait)
        ratio = get_ratio(self.gears, depth=depth)
        super(MotorExt, self).run_angle(speed / ratio,
                                        rotation_angle / ratio,
                                        stop_type=stop_type,
                                        wait=wait)

    def output_percent_run_angle(self, speed, rotation_angle, stop_type=Stop.COAST,
                                 wait=True, rpm=240, depth=None):
        """Keep the motor or linked gears running at a constant speed (percentage) for a
        speicified amount of degrees

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param rotation_angle: Angle (degrees) by which the Motor should run
        :type rotation_angle: int
        :param stop_type: Whether to coast, brake, or hold after coming to a tandstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            self.percent_run_angle(speed, rotation_angle, stop_type=stop_type, wait=wait, rpm=rpm)
        ratio = get_ratio(self.gears, depth=depth)
        super(MotorExt, self).run_angle(speed_deg(speed, rpm=rpm) / ratio,
                                        rotation_angle / ratio, stop_type=stop_type, wait=wait)

    def percent_run_angle(self, speed, rotation_angle, stop_type=Stop.COAST, wait=True, rpm=240):
        """Keep the motor running at a constant speed (percentage) for a
        speicified amount of degrees

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param rotation_angle: Angle (degrees) by which the Motor should run
        :type rotation_angle: int
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        """
        super(MotorExt, self).run_angle(speed_deg(speed, rpm=rpm),
                                        rotation_angle, stop_type=stop_type, wait=wait)

    def output_run_target(self, speed, target_angle, stop_type=Stop.COAST, wait=True, depth=None):
        """Keep the motor or linked gears running at a constant speed towards a
        speicified target degree

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param target_angle: Target angle that the Motor should rotate to,
        regardless of its current angle
        :type target_angle: int
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            super(MotorExt, self).run_target(speed, target_angle, stop_type=stop_type, wait=wait)
        ratio = get_ratio(self.gears, depth=depth)
        super(MotorExt, self).run_target(speed / ratio, target_angle / ratio,
                                         stop_type=stop_type, wait=wait)

    def output_percent_run_target(self, speed, target_angle, stop_type=Stop.COAST,
                                  wait=True, rpm=240, depth=None):
        """Keep the motor or linked gears running at a constant speed (percentage) towards a
        speicified target degree

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear (percentage)
        :type speed: int, float
        :param target_angle: Target angle that the Motor should rotate to,
        regardless of its current angle
        :type target_angle: int
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            self.percent_run_target(speed, target_angle, stop_type=stop_type, wait=wait, rpm=rpm)
        ratio = get_ratio(self.gears, depth=depth)
        super(MotorExt, self).run_target(speed_deg(speed, rpm=rpm) / ratio,
                                         target_angle / ratio, stop_type=stop_type, wait=wait)

    def percent_run_target(self, speed, target_angle, stop_type=Stop.COAST, wait=True, rpm=240):
        """Keep the motor running at a constant speed (percentage) towards a
        speicified target degree

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear (percentage)
        :type speed: int, float
        :param target_angle: Target angle that the Motor should rotate to,
        regardless of its current angle
        :type target_angle: int
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param wait: Whether to wait for the maneuver to complete before continuing with the rest of
        the program, defaults to True
        :type wait: bool, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        """
        super(MotorExt, self).run_target(speed_deg(speed, rpm=rpm), target_angle,
                                         stop_type=stop_type, wait=wait)

    def output_run_until_stalled(self, speed, stop_type=Stop.COAST, duty_limit=100, depth=None):
        """Keep the motor or linked gears running at a constant speed until it stalls

        :param speed: Speed of the Motor or Gear
        :type speed: int, float
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param duty_limit: Relative torque limit, defaults to 100
        :type duty_limit: int, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            super(MotorExt, self).run_until_stalled(speed, stop_type=stop_type,
                                                    duty_limit=duty_limit)
        super(MotorExt, self).run_until_stalled(speed / get_ratio(self.gears, depth=depth),
                                                stop_type=stop_type, duty_limit=duty_limit)

    def output_percent_run_until_stalled(self, speed, stop_type=Stop.COAST,
                                         duty_limit=100, rpm=240, depth=None):
        """Keep the motor or linked gears running at a constant speed (percentage) until it stalls

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear (percentage)
        :type speed: int, float
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param duty_limit: Relative torque limit, defaults to 100
        :type duty_limit: int, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        :param depth: Depth of the gear in the link to set the speed for, defaults to None
        :type depth: int, optional
        """
        if depth is None:
            self.percent_run_until_stalled(speed, stop_type=stop_type,
                                           duty_limit=duty_limit, rpm=rpm)
        super(MotorExt, self).run_until_stalled(
            speed_deg(speed, rpm=rpm) * get_ratio(self.gears, depth=depth),
            stop_type=stop_type, duty_limit=duty_limit)

    def percent_run_until_stalled(self, speed, stop_type=Stop.COAST, duty_limit=100, rpm=240):
        """Keep the motor running at a constant speed (percentage) until it stalls

        Medium Motor    - 240 RPM
        Large Motor     - 160 RPM

        :param speed: Speed of the Motor or Gear (percentage)
        :type speed: int, float
        :param stop_type: Whether to coast, brake, or hold after coming to a standstill,
        defaults to Stop.COAST
        :type stop_type: Stop, optional
        :param duty_limit: Relative torque limit, defaults to 100
        :type duty_limit: int, optional
        :param rpm: RPM of the motor, defaults to 240
        :type rpm: int, optional
        """
        super(MotorExt, self).run_until_stalled(speed_deg(speed, rpm=rpm),
                                                stop_type=stop_type, duty_limit=duty_limit)

    def wait_until_motor_stop(self):
        """
        Waits until the motor stops
        """
        while super(MotorExt, self).speed() != 0:
            wait(10)
        return

    def wait_until_motor_start(self):
        """
        Waits until the motor starts
        """
        while super(MotorExt, self).speed() == 0:
            wait(10)
        return

    def wait_until_motor_speed(self, operator, speed):
        """Waits until the motor speed matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param speed: Speed to calculate against (Motor.speed <OP> speed)
        :type speed: int, float
        """
        while not _operator_calc(super(MotorExt, self).speed(), speed, operator):
            wait(10)
        return

class TouchSensorExt(TouchSensor):
    """
    Extension class for the TouchSensor with helpful
    methods mainly relating to wait functions

    Further documentation for the TouchSensor class can be found
    'https://klutzybubbles.github.io/lego-micropython-docs/ev3devices.html#ev3devices.TouchSensor'

    :param port: Port to which the sensor is connected
    :type port: Port
    """

    def wait_until_pressed(self):
        """
        Wait until the TouchSensor is pressed
        """
        while not super(TouchSensorExt, self).pressed():
            wait(10)
        return

    def wait_until_released(self):
        """
        Wait until the TouchSensor is released
        """
        while super(TouchSensorExt, self).pressed():
            wait(10)
        return

    def wait_until_bumped(self, wait_timer=500):
        """Wait until the TouchSensor is bumped

        :param wait_timer: Time to wait (milliseconds) to consider a press and release a bump,
        defaults to 500
        :type wait_timer: int, float, optional
        """
        if not isinstance(wait_timer, (int, float)):
            return
        my_watch = StopWatch()
        while True:
            self.wait_until_pressed()
            my_watch.reset()
            my_watch.resume()
            self.wait_until_released()
            my_watch.pause()
            if my_watch.time() > wait_timer:
                continue
            return

class ColorSensorExt(ColorSensor):
    """Extension class for the ColorSensor with helpful methods

    Further documentation for the ColorSensor class can be found
    'https://klutzybubbles.github.io/lego-micropython-docs/ev3devices.html#ev3devices.ColorSensor'

    :param port: Port to which the sensor is connected
    :type port: Port
    """

    def equals(self, color):
        """Checks whether the color equals a Color or a set of Colors

        See ColorExt for color values
        list, tuple or dict must have values of instance Color

        :param color: Color to compare sensor color to
        :type color: Color, int, float, list, tuple, dict
        :return: Whether or not the color is equal or is contained
        :rtype: bool
        """
        return ColorExt.compare(color, super(ColorSensorExt, self).color())

    def wait_until_color_is(self, color):
        """Waits until the color equals a Color or a set of Colors

        See ColorExt for color values
        list, tuple or dict must have values of instance Color

        :param color: Color to compare sensor color to
        :type color: Color, int, float, list, tuple, dict
        """
        while not self.equals(color):
            wait(10)
        return

    def wait_until_color_not(self, color):
        """Waits until the color does not equal a Color or a set of Colors

        See ColorExt for color values
        list, tuple or dict must have values of instance Color

        :param color: Color to compare sensor color to
        :type color: Color, int, float, list, tuple, dict
        """
        while self.equals(color):
            wait(10)
        return

    def wait_until_ambient(self, operator, ambient):
        """Waits until the ambient color matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param ambient: Ambient value to calculate against (ColorSensor.ambient <OP> ambient)
        :type ambient: int, float
        """
        while not _operator_calc(super(ColorSensorExt, self).ambient(), ambient, operator):
            wait(10)
        return

    def wait_until_reflection(self, operator, reflection):
        """Waits until the reflection color matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param reflection: Reflection value to calculate against
        (ColorSensor.reflection <OP> reflection)
        :type reflection: int, float
        """
        while not _operator_calc(super(ColorSensorExt, self).reflection(), reflection, operator):
            wait(10)
        return

    def rgb_255(self):
        """Measure the reflection of a surface using a red, green, and then a blue light.

        :return: Reflection for red, green, and blue light, each ranging from
        0.0 (no reflection) to 255.0 (high reflection).
        :rtype: tuple
        """
        rgb = super(ColorSensorExt, self).rgb()
        base = 255 / 100
        return (base * rgb[0], base * rgb[1], base * rgb[2])

    def hex(self):
        """Measure the color of a surface in the form of a hex string

        :return: Color measured in hex value
        :rtype: str
        """
        return '%02x%02x%02x' & self.rgb_255()

    def hsv(self):
        """Measure the color of a surface in the form of Hue, Saturation and Value

        :return: Color measured in the form (h, s, v)
        :rtype: tuple
        """
        rgb = super(ColorSensorExt, self).rgb()
        r, g, b = rgb[0] / 100.0, rgb[1] / 100.0, rgb[2] / 100.0
        mx = max(r, g, b)
        mn = min(r, g, b)
        df = mx - mn
        if mx == mn:
            h = 0
        elif mx == r:
            h = (60 * ((g - b) / df) + 360) % 360
        elif mx == g:
            h = (60 * ((b - r) / df) + 120) % 360
        elif mx == b:
            h = (60 * ((r - g) / df) + 240) % 360
        if mx == 0:
            s = 0
        else:
            s = (df / mx) * 100
        v = mx * 100
        return h, s, v

    def hue(self):
        """Measure the hue of a surface

        :return: Hue of the surface calculated from ColorSensor.rgb()
        :rtype: int, float
        """
        return self.hsv()[0]

class InfraredSensorExt(InfraredSensor):
    """Extension class for the InfraredSensor with helpful methods

    Further documentation for the InfraredSensor class can be found
    'http://klutzybubbles.github.io/lego-micropython-docs/ev3devices.html#ev3devices.InfraredSensor'

    :param port: Port to which the sensor is connected
    :type port: Port
    """

    def beacon_distance(self, channel):
        """Measure the relative distance between the remote and the infrared sensor

        :param channel: Channel number of the remote
        :type channel: int
        :return: Relative distance between the remote and the infrared sensor
        :rtype: int, float
        """
        return super(InfraredSensorExt, self).beacon(channel)[0]

    def beacon_angle(self, channel):
        """Measure the relative angle to the remote and the infrared sensor

        :param channel: Channel number of the remote
        :type channel: int
        :return: Relative angle to the remote and the infrared sensor
        :rtype: int
        """
        return super(InfraredSensorExt, self).beacon(channel)[1]

    def wait_until_distance(self, operator, distance):
        """Waits until the distance matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param distance: Distance value to calculate against (InfraredSensor.distance <OP> distance)
        :type distance: int, float
        """
        while not _operator_calc(super(InfraredSensorExt, self).distance(), distance, operator):
            wait(10)
        return

    def wait_until_beacon_distance(self, operator, beacon_distance, channel):
        """Waits until the beacon distance matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param beacon_distance: Beacon distance value to calculate against
        (InfraredSensorExt.beacon_distance <OP> beacon_distance)
        :type beacon_distance: int, float
        :param channel: Channel number of the remote
        :type channel: int
        """
        while not _operator_calc(self.beacon_distance(channel), beacon_distance, operator):
            wait(10)
        return

    def wait_until_beacon_angle(self, operator, beacon_angle, channel):
        """Waits until the beacon angle matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param beacon_angle: Beacon angle value to calculate against
        (InfraredSensorExt.beacon_angle <OP> beacon_angle)
        :type beacon_angle: int, float
        :param channel: Channel number of the remote
        :type channel: int
        """
        while not _operator_calc(self.beacon_angle(channel), beacon_angle, operator):
            wait(10)
        return

    def wait_until_button_pressed(self, button, channel):
        """Waits until a specified button has been pressed

        :param button: Button or Buttons to wait for
        :type button: Button, list, tuple, dict
        :param channel: Channel number of the remote
        :type channel: int
        """
        if isinstance(button, (list, tuple, dict)):
            while True:
                buttons = super(InfraredSensorExt, self).buttons(channel)
                for one_button in button:
                    if one_button in buttons:
                        return
                wait(10)
        else:
            while button not in super(InfraredSensorExt, self).buttons(channel):
                wait(10)
        return

    def wait_until_button_released(self, button, channel):
        """Waits until a specified button has been released

        :param button: Button or Buttons to wait for
        :type button: Button, list, tuple, dict
        :param channel: Channel number of the remote
        :type channel: int
        """
        if isinstance(button, (list, tuple, dict)):
            while True:
                buttons = super(InfraredSensorExt, self).buttons(channel)
                for one_button in button:
                    if one_button not in buttons:
                        return
                wait(10)
        else:
            while button in super(InfraredSensorExt, self).buttons(channel):
                wait(10)
        return

    def wait_until_button_bumped(self, button, channel, wait_timer=500):
        """Waits until a specified button has been bumped

        ''NOTE: using a list, tuple or dict for buttons will make this function act the same as
        wait_until_button_pressed if all of the buttons listed are pressed at once''

        :param button: Button or Buttons to wait for
        :type button: Button, list, tuple, dict
        :param channel: Channel number of the remote
        :type channel: int
        """
        if not isinstance(wait_timer, (int, float)):
            return
        my_watch = StopWatch()
        while True:
            self.wait_until_button_pressed(button, channel)
            my_watch.reset()
            my_watch.resume()
            self.wait_until_button_released(button, channel)
            my_watch.pause()
            if my_watch.time() > wait_timer:
                continue
            return

class UltrasonicSensorExt(UltrasonicSensor):
    """Extension class for the UltrasonicSensor with helpful methods

    Further documentation for the UltrasonicSensor class can be found
    'klutzybubbles.github.io/lego-micropython-docs/ev3devices.html#ev3devices.UltrasonicSensor'

    :param port: Port to which the sensor is connected
    :type port: Port
    """

    def wait_until_distance(self, operator, distance):
        """Waits until the distance matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param distance: Distance value to calculate against
        (UltrasonicSensor.distance <OP> distance)
        :type distance: int, float
        """
        while not _operator_calc(super(UltrasonicSensorExt, self).distance(), distance, operator):
            wait(10)
        return

    def wait_until_presence(self):
        """
        Waits until the UltrasonicSensor detects the presence of another UltrasonicSensor
        """
        while not super(UltrasonicSensorExt, self).presence():
            wait(10)

    def wait_until_not_presence(self):
        """
        Waits until the UltrasonicSensor doesn't detect the presence of another UltrasonicSensor
        """
        while super(UltrasonicSensorExt, self).presence():
            wait(10)

class GyroSensorExt(GyroSensor):
    """Extension class for the GyroSensor with helpful methods

    Further documentation for the GyroSensor class can be found
    'https://klutzybubbles.github.io/lego-micropython-docs/ev3devices.html#ev3devices.GyroSensor'

    :param port: Port to which the sensor is connected
    :type port: Port
    """

    def __init__(self, port):
        """
        Initiate the GyroSensorExt Object
        """
        super(GyroSensorExt, self).__init__(port)

    def speed_rotations(self):
        """Gets the speed (angular velocity) of the sensor in rotations a second

        :return: Sensor angular velocity in rotations a second
        :rtype: int, float
        """
        return super(GyroSensorExt, self).speed() / 360

    def bearing(self):
        """Gets the current bearing of the sensor

        :return: Current bearing of the sensor from 0 to 360
        :rtype: int
        """
        return super(GyroSensorExt, self).angle() % 360

    def angle_rotations(self):
        """Gets the accumulated angle of the sensor in rotations

        :return: Rotation angle
        :rtype: int, float
        """
        return super(GyroSensorExt, self).angle() / 360

    def reset_angle_bearing(self, angle):
        """Sets the rotation angle of the sensor to the bearing of an angle

        :param angle: Value to which the beaing should be calculated from
        :type angle: int
        """
        super(GyroSensorExt, self).reset_angle(angle % 360)

    def wait_until_speed(self, operator, speed):
        """Waits until the speed matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param speed: Speed value to calculate against (GyroSensor.speed <OP> speed)
        :type speed: int, float
        """
        while not _operator_calc(super(GyroSensorExt, self).speed(), speed, operator):
            wait(10)
        return

    def wait_until_angle(self, operator, angle):
        """Waits until the angle matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param angle: Angle value to calculate against (GyroSensor.angle <OP> angle)
        :type angle: int, float
        """
        while not _operator_calc(super(GyroSensorExt, self).angle(), angle, operator):
            wait(10)
        return

    def wait_until_speed_rotations(self, operator, speed):
        """Waits until the speed in rotations matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param speed: Speed rotations value to calculate against
        (GyroSensorExt.speed_rotations <OP> speed)
        :type speed: int, float
        """
        while not _operator_calc(self.speed_rotations(), speed, operator):
            wait(10)
        return

    def wait_until_angle_rotations(self, operator, angle):
        """Waits until the angle in rotations matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param angle: Angle rotations value to calculate against
        (GyroSensorExt.angle_rotations <OP> angle)
        :type angle: int, float
        """
        while not _operator_calc(self.angle_rotations(), angle, operator):
            wait(10)
        return

    def wait_until_bearing(self, operator, bearing):
        """Waits until the bearing matches certain conditions

        :param operator: Operator to be used for the calculation (>, <, <=, >=, ==, !=)
        :type operator: str
        :param bearing: Bearing value to calculate against (GyroSensorExt.bearing <OP> bearing)
        :type bearing: int, float
        """
        while not _operator_calc(self.bearing(), bearing, operator):
            wait(10)
        return
