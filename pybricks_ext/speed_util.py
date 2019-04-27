def float_percent(percent, min_percent=-100, max_percent=100):
    """Converts a whole percentage (100, 50) to a floating point percentage (1, 0.5).

    Adds validation to make sure that the percent is always between min and max.
    
    :param percent: The percentage to convert
    :type percent: int, float
    :param min_percent: Minimum percentage to accept, defaults to -100
    :type min_percent: int, float, optional
    :param max_percent: Maximum percentage to accept, defaults to 100
    :type max_percent: int, float, optional
    :return: The floating point percentage between the min and max
    :rtype: int, float
    """
    if min_percent > max_percent:
        temp_percent = min_percent
        min_percent = max_percent
        max_percent = temp_percent
    elif min_percent == max_percent:
        return min_percent
    if percent is None or not isinstance(percent, (int, float)):
        if 0 >= min_percent and 0 <= max_percent:
            return 0
        return (min_percent + max_percent) / 2
    if percent > max_percent:
        percent = max_percent
    elif percent < min_percent:
        percent = min_percent
    return percent / 100

def speed_mm(percent, rpm=160, wheel_diam=56, min_percent=-100, max_percent=100):
    """[Translates speed in percentage to speed in mm/s to help with DriveBase methods.

    Medium Motor    - 240 RPM
    Large Motor     - 160 RPM
    Lego EV3 Wheels - 56 MM

    :param percent: Speed to get (in %)
    :type percent: int, float
    :param rpm: RPM of motor, defaults to 160
    :type rpm: int, optional
    :param wheel_diam: Diameter of wheels in mm, defaults to 56
    :type wheel_diam: int, float, optional
    :param min_percent: Minimum precentage, defaults to -100
    :type min_percent: int, float, optional
    :param max_percent: Maximum percentage, defaults to 100
    :type max_percent: int, float, optional
    :return: Speed in mm/s
    :rtype: int, float
    """
    multiplier = float_percent(percent, min_percent, max_percent)
    max_speed = (rpm / 60) * (wheel_diam * math.pi)
    return max_speed * multiplier

def speed_deg(percent, rpm=240, min_percent=-100, max_percent=100):
    """Translates speed in percentage to speed in deg/s to help with Motor run methods.

    Medium Motor    - 240 RPM
    Large Motor     - 160 RPM

    :param percent: Speed to get (in %)
    :type percent: int, float
    :param rpm: RPM of motor, defaults to 240
    :type rpm: int, optional
    :param min_percent: Minimum precentage, defaults to -100
    :type min_percent: int, float, optional
    :param max_percent: Maximum percentage, defaults to 100
    :type max_percent: int, float, optional
    :return: Speed in deg/s
    :rtype: int, float
    """
    multiplier = float_percent(percent, min_percent, max_percent)
    max_speed = (rpm / 60) * 360
    return max_speed * multiplier

def speed_mm_deg(speed, wheel_diam=56):
    """Translates speed in mm/s to speed in deg/s to help with Motor run methods

    Lego EV3 Wheels - 56 MM

    :param speed: Speed to translate (in mm/s)
    :type speed: int, float
    :param wheel_diam: Diameter of the wheels in MM, defaults to 56
    :type wheel_diam: int, float, optional
    :return: Speed in deg/s
    :rtype: int, float
    """
    rotations = speed / (wheel_diam * math.pi)
    return rotations * 360

def speed_deg_mm(speed, wheel_diam=56):
    """Translates speed in deg/s to speed in mm/s to help with Motor run methods

    Lego EV3 Wheels - 56 MM

    :param speed: Speed to translate (in deg/s)
    :type speed: int, float
    :param wheel_diam: Diameter of the wheels in MM, defaults to 56
    :type wheel_diam: int, float, optional
    :return: Speed in mm/s
    :rtype: int, float
    """
    rotations = speed / 360
    return rotations * (wheel_diam * math.pi)

def get_ratio(gears, depth=None):
    """Gets the ratio of a list or Tuple of gears.

    It is reccomended to use a Tuple as genrally gear
    ratios are not going to be changed dynamically.

    This method should NOT be used as a replacement for
    the inbuilt motor gear ratios.

    :param gears: List of gears from input to output, gear trains can be used by nesting lists or tuples inside
    :type gears: list, tuple
    :param depth: Depth of train gears to get the ratio for, works like array pointers or you can set it to None to ignore it, defaults to None
    :type depth: int, optional
    :return: Gear ratio floating point
    :rtype: int, float
    """
    if (not isinstance(gears, (list, tuple))
        or gears is None
        or len(gears) is 0
        or not isinstance(gears[0], (list, tuple, int, float))):
        return 1
    if (not isinstance(depth, int)
        or depth < 0
        or depth >= len(gears)):
        depth = len(gears) - 1
    if depth == 0:
        return 1
    ratio = 1
    current_depth = 0
    if isinstance(gears[0], (list, tuple)):
        for loop in range(0, len(gears)):
            for inner_loop in range(0, len(gears[loop])):
                if inner_loop + 1 is len(gears[loop]):
                    break
                ratio *= gears[loop][inner_loop] / gears[loop][inner_loop + 1]
                current_depth += 1
                if current_depth > depth:
                    break
            if current_depth > depth:
                break
    else:
        for loop in range(0, len(gears)):
            if loop + 1 is len(gears):
                break
            ratio *= gears[loop] / gears[loop + 1]
            current_depth += 1
            if current_depth > depth:
                break
    return ratio
