Signals and Units
=================

Many commands allow you to specify arguments in terms of well-known physical
quantities. This page gives an overview of each quantity and its unit.

.. _time:

time: ms
---------
All time and duration values are measured in milliseconds (ms).

For example, the duration of motion with
:meth:`output_run_time <.ev3devices_ext.MotorExt.output_run_time>`, the
duration of :func:`wait <.tools_ext.wait>`, or the time values returned by the
:class:`StopWatchExt <.tools_ext.StopWatchExt>` are specified in milliseconds.

.. _angle:

angle: deg
-----------
All angles are measured in degrees (deg). One full rotation corresponds to
360 degrees.

For example, the angle values of a
:meth:`MotorExt <.ev3devices_ext.MotorExt.output_angle>` or the
:meth:`GyroSensorExt <.ev3devices_ext.GyroSensorExt.bearing>` are
expressed in degrees.

.. _speed:

rotational speed: deg/s
-----------------------

Rotational speed, or *angular velocity* describes how fast something rotates,
expressed as the number of degrees per second (deg/s).

For example, the rotational speed values of a
:meth:`MotorExt <.ev3devices.MotorExt.output_speed>` or the
:meth:`GyroSensorExt <.ev3devices.GyroSensorExt.speed>`
are expressed in degrees per second.

While we recommend working with degrees per second in your programs, you can
use the following table to convert between commonly used units.

+-----------+-------+-----------+--------------+
|           | deg/s | rpm       | rot/s        |
+-----------+-------+-----------+--------------+
| 1 deg/s = | 1     | 1/6=0.167 | 1/360=0.0027 |
+-----------+-------+-----------+--------------+
| 1 rpm   = | 6     | 1         | 1/60=0.0167  |
+-----------+-------+-----------+--------------+
| 1 rot/s = | 360   | 60        | 1            |
+-----------+-------+-----------+--------------+

.. _distance:

distance: mm
-------------
Distances are expressed in millimeters (mm) whenever possible.

For example, the distance value of the
:meth:`UltrasonicSensorExt
<.ev3devices_ext.UltrasonicSensorExt.wait_until_distance>`
is measured in millimeters.

While we recommend working with millimeters in your programs, you can use the
following table to convert between commonly used units.

+---------+------+-----+--------+
|         | mm   | cm  | inch   |
+---------+------+-----+--------+
| 1 mm =  | 1    | 0.1 | 0.0394 |
+---------+------+-----+--------+
| 1 cm =  | 10   | 1   | 0.394  |
+---------+------+-----+--------+
| 1 inch =| 25.4 | 2.54| 1      |
+---------+------+-----+--------+

.. _dimension:

dimension: mm
-------------
Dimensions are expressed in millimeters (mm) whenever possible, just like
distances.

For example, the diameter of a wheel is measured in millimeters.

.. _relativedistance:

relative distance: %
---------------------

Some distance measurements do not provide an accurate value with a specific
unit, but they range from very close (0%) to very far (100%). These are
referred to as relative distances.

For example, the distance value of the
:meth:`InfraredSensorExt
<.ev3devices_ext.InfraredSensorExt.wait_until_distance>`
is a relative distance.

.. _travelspeed:

speed: mm/s
------------
Linear speeds are expressed as millimeters per second (mm/s).

For example, the speed of a robotic vehicle is expressed in mm/s.

.. _percentage:

percentage: %
--------------
Some signals do not have specific units but range from a minimum (0%) to a
maximum (100%). A specific type of percentages are
:ref:`relative distances <relativedistance>`.

For example, the sound :meth:`volume <.ev3brick_ext.sound.beep>` ranges from
0% to 100%.

A percentage when coding can be represented as a
floating point from 0.0 to 1.0. It can also go to -1.0

.. _percentagewhole:

percentage whole: %
-------------------
This is the whole number representation of the percentage (100 for 100%)

For example, the sound :meth:`volume <.ev3brick_ext.sound.beep>` ranges from
0% to 100%.

.. _rpm:

RPM
---
RPM (Rotations per minute) is as the name suggests, the amount of Rotations
something makes within 1 minute. For the extension library this is usually
only used for setting a motors max speed.

.. _frequency:

frequency: Hz
--------------
Sound frequencies are expressed in Hertz (Hz).

For example, you can choose the frequency of a
:meth:`beep <.ev3brick_ext.sound.beep>` to change the pitch.
