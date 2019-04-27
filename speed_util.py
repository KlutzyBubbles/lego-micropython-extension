'''
Converts a whole percentage (100, 50) to a floating point percentage (1, 0.5).

Adds validation to make sure that the percent is always between min and max.

percent     - The percentage to convert (int, float)
min_percent - Minimum percentage to accept (default -100)
max_percent - Maximum percentage to accept (default 100)

return      - The floating point percentage between the min and max
'''
def float_percent(percent, min_percent=-100, max_percent=100):
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
'''
Translates speed in percentage to speed in mm/s to help
with DriveBase methods.

Medium Motor    - 240 RPM
Large Motor     - 160 RPM
Lego EV3 Wheels - 56 MM

percent     - Speed to get (in %)
rpm         - RPM of motor (default 160)
wheel_diam  - Diameter of wheels in mm (default 56)
min_percent - Minimum precentage (default -100)
max_percent - Maximum percentage (default 100)

return      - Speed in mm/s
'''
def speed_mm(percent, rpm=160, wheel_diam=56, min_percent=-100, max_percent=100):
    multiplier = float_percent(percent, min_percent, max_percent)
    max_speed = (rpm / 60) * (wheel_diam * math.pi)
    return max_speed * multiplier

'''
Translates speed in percentage to speed in deg/s to help
with Motor run methods.

Medium Motor    - 240 RPM
Large Motor     - 160 RPM

percent     - Speed to get (in %)
rpm         - RPM of motor (default 240)
min_percent - Minimum precentage (default -100)
max_percent - Maximum percentage (default 100)

return      - Speed in deg/s
'''
def speed_deg(percent, rpm=240, min_percent=-100, max_percent=100):
    multiplier = float_percent(percent, min_percent, max_percent)
    max_speed = (rpm / 60) * 360
    return max_speed * multiplier

'''
Translates speed in mm/s to speed in deg/s to help
with Motor run methods

Lego EV3 Wheels - 56 MM

speed       - Speed to translate (in mm/s)
wheel_diam  - Diameter of the wheels in MM (default 56)

return      - Speed in deg/s
'''
def speed_mm_deg(speed, wheel_diam=56):
    rotations = speed / (wheel_diam * math.pi)
    return rotations * 360

'''
Translates speed in deg/s to speed in mm/s to help
with Motor run methods

Lego EV3 Wheels - 56 MM

speed       - Speed to translate (in deg/s)
wheel_diam  - Diameter of the wheels in MM (default 56)

return      - Speed in mm/s
'''
def speed_deg_mm(speed, wheel_diam=56):
    rotations = speed / 360
    return rotations * (wheel_diam * math.pi)

'''
Gets the ratio of a list or Tuple of gears.

It is reccomended to use a Tuple as genrally gear
ratios are not going to be changed dynamically.

This method should NOT be used as a replacement for
the inbuilt motor gear ratios.

gears       - List or Tuple of gears from input to output gear
              trains can be used by nesting lists or tuples inside
depth       - Amount of gears (or depth of train gears) to get the
              ratio for, works like array pointers or you can set
              it to None to ignore it (default=None)

return      - Gear ratio floating point
'''
def get_ratio(gears, depth=None):
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
