from math import pi

def float_percent(percent, min_percent=-100, max_percent=100):
    """Converts a whole percentage (``100``, ``50``) to a floating point percentage (``1``, ``0.5``).

    Adds validation to make sure that the percent is always between min and max.

    :param percent: The percentage to convert
    :type percent: :ref:`percentagewhole`
    :param min_percent: Minimum percentage to accept (Default: ``-100``)
    :type min_percent: :ref:`percentagewhole`
    :param max_percent: Maximum percentage to accept (Default: ``100``)
    :type max_percent: :ref:`percentagewhole`
    :return: The floating point percentage between the min and max
    :rtype: :ref:`percentage`
    """
    if min_percent > max_percent:
        temp_percent = min_percent
        min_percent = max_percent
        max_percent = temp_percent
    elif min_percent == max_percent:
        return min_percent
    if percent is None or not isinstance(percent, (int, float)):
        if min_percent <= 0 and max_percent >= 0:
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

    :param percent: Speed to get (%)
    :type percent: :ref:`percentage`
    :param rpm: RPM of motor (Default: ``160``)
    :type rpm: :ref:`rpm`
    :param wheel_diam: Diameter of wheels in mm (Default: ``56``)
    :type wheel_diam: :ref:`dimension`
    :param min_percent: Minimum precentage (Default: ``-100``)
    :type min_percent: :ref:`percentagewhole`
    :param max_percent: Maximum percentage (Default: ``100``)
    :type max_percent: :ref:`percentagewhole`

    :return: Speed in mm/s
    :rtype: :ref:`travelspeed`
    """
    multiplier = float_percent(percent, min_percent, max_percent)
    max_speed = (rpm / 60) * (wheel_diam * pi)
    return max_speed * multiplier

def speed_deg(percent, rpm=240, min_percent=-100, max_percent=100):
    """Translates speed in percentage to speed in deg/s to help with Motor run methods.

    Medium Motor    - 240 RPM
    Large Motor     - 160 RPM
    
    :param percent: Speed to get (%)
    :type percent: :ref:`percentage`
    :param rpm: RPM of motor (Default: ``240``)
    :type rpm: :ref:`rpm`
    :param min_percent: Minimum precentage (Default: ``-100``)
    :type min_percent: :ref:`percentagewhole`
    :param max_percent: Maximum percentage (Default: ``100``)
    :type max_percent: :ref:`percentagewhole`
    
    :return: Speed in deg/s
    :rtype: :ref:`speed`
    """
    multiplier = float_percent(percent, min_percent, max_percent)
    max_speed = (rpm / 60) * 360
    return max_speed * multiplier

def speed_mm_deg(speed, wheel_diam=56):
    """Translates speed in mm/s to speed in deg/s to help with Motor run methods

    Lego EV3 Wheels - 56 MM

    :param speed: Speed to translate (mm/s)
    :type speed: :ref:`travelspeed`
    :param wheel_diam: Diameter of wheels in mm (Default: ``56``)
    :type wheel_diam: :ref:`dimension`
    :return: Speed in deg/s
    :rtype: :ref:`speed`
    """
    rotations = speed / (wheel_diam * pi)
    return rotations * 360

def speed_deg_mm(speed, wheel_diam=56):
    """Translates speed in deg/s to speed in mm/s to help with Motor run methods

    Lego EV3 Wheels - 56 MM

    :param speed: Speed to translate (deg/s)
    :type speed: :ref:`speed`
    :param wheel_diam: Diameter of wheels in mm (Default: ``56``)
    :type wheel_diam: :ref:`dimension`
    :return: Speed in mm/s
    :rtype: :ref:`travelspeed`
    """
    rotations = speed / 360
    return rotations * (wheel_diam * pi)

def get_ratio(gears, depth=None):
    """Gets the ratio of a list or Tuple of gears.

    It is reccomended to use a Tuple as genrally gear ratios are not going to be changed dynamically.

    This method should NOT be used as a replacement for the inbuilt motor gear ratios.

    :param gears: List of gears from input to output, gear trains can be used by nesting lists or tuples inside
    :type gears: list, tuple
    :param depth: Depth of train gears to get the ratio for, works like array pointers or you can set it to ``None`` to ignore it (Default: ``None``)
    :type depth: int

    :return: Gear ratio floating point
    :rtype: float
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
        for loop in enumerate(gears):
            for inner_index, inner_loop in enumerate(loop, 1):
                ratio *= loop[inner_index - 1] / inner_loop
                current_depth += 1
                if current_depth > depth:
                    break
            if current_depth > depth:
                break
    else:
        for index, loop in enumerate(gears, 1):
            ratio *= gears[index - 1] / loop
            current_depth += 1
            if current_depth > depth:
                break
    return ratio
