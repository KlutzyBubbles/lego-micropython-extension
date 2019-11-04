:mod:`ev3devices` -- EV3 Motor and Sensor Extension Classes
===============================================================

.. automodule:: ev3devices
    :no-members:

Motor
-----

.. autoclass:: ev3devices.Motor
    :no-members:

    **Motor Information**

    .. automethod:: ev3devices.Motor.output_angle

    .. automethod:: ev3devices.Motor.output_speed

    **Run**

    .. automethod:: ev3devices.Motor.output_run

    .. automethod:: ev3devices.Motor.output_percent_run

    .. automethod:: ev3devices.Motor.percent_run

    **Run Time**

    .. automethod:: ev3devices.Motor.output_run_time

    .. automethod:: ev3devices.Motor.output_percent_run_time

    .. automethod:: ev3devices.Motor.percent_run_time

    **Run Angle**

    .. automethod:: ev3devices.Motor.output_run_angle

    .. automethod:: ev3devices.Motor.output_percent_run_angle

    .. automethod:: ev3devices.Motor.percent_run_angle

    **Run Target**

    .. automethod:: ev3devices.Motor.output_run_target

    .. automethod:: ev3devices.Motor.output_percent_run_target

    .. automethod:: ev3devices.Motor.percent_run_target

    Advanced methods for motors with rotation sensors

    **Run Until Stalled**

    .. automethod:: ev3devices.Motor.output_run_until_stalled

    .. automethod:: ev3devices.Motor.output_percent_run_until_stalled

    .. automethod:: ev3devices.Motor.percent_run_until_stalled

Sensors
-------

Touch Sensor
^^^^^^^^^^^^
.. autoclass:: ev3devices.TouchSensor
    :members:

Color Sensor
^^^^^^^^^^^^
.. autoclass:: ev3devices.ColorSensor
    :members:

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices.InfraredSensor
    :members:

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices.UltrasonicSensor
    :members:

Gyroscopic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices.GyroSensor
    :members:
