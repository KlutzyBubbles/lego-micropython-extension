:mod:`ev3devices_ext` -- EV3 Motor and Sensor Extension Classes
===============================================================

.. automodule:: ev3devices_ext
    :no-members:

Motor
-----

.. autoclass:: ev3devices_ext.MotorExt
    :no-members:

    **Motor Information**

    .. automethod:: ev3devices_ext.MotorExt.output_angle

    .. automethod:: ev3devices_ext.MotorExt.output_speed

    **Run**

    .. automethod:: ev3devices_ext.MotorExt.output_run

    .. automethod:: ev3devices_ext.MotorExt.output_percent_run

    .. automethod:: ev3devices_ext.MotorExt.percent_run

    **Run Time**

    .. automethod:: ev3devices_ext.MotorExt.output_run_time

    .. automethod:: ev3devices_ext.MotorExt.output_percent_run_time

    .. automethod:: ev3devices_ext.MotorExt.percent_run_time

    **Run Angle**

    .. automethod:: ev3devices_ext.MotorExt.output_run_angle

    .. automethod:: ev3devices_ext.MotorExt.output_percent_run_angle

    .. automethod:: ev3devices_ext.MotorExt.percent_run_angle

    **Run Target**

    .. automethod:: ev3devices_ext.MotorExt.output_run_target

    .. automethod:: ev3devices_ext.MotorExt.output_percent_run_target

    .. automethod:: ev3devices_ext.MotorExt.percent_run_target

    Advanced methods for motors with rotation sensors

    **Run Until Stalled**

    .. automethod:: ev3devices_ext.MotorExt.output_run_until_stalled

    .. automethod:: ev3devices_ext.MotorExt.output_percent_run_until_stalled

    .. automethod:: ev3devices_ext.MotorExt.percent_run_until_stalled

Sensors
-------

Touch Sensor
^^^^^^^^^^^^
.. autoclass:: ev3devices_ext.TouchSensorExt
    :members:

Color Sensor
^^^^^^^^^^^^
.. autoclass:: ev3devices_ext.ColorSensorExt
    :members:

Infrared Sensor and Beacon
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices_ext.InfraredSensorExt
    :members:

Ultrasonic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices_ext.UltrasonicSensorExt
    :members:

Gyroscopic Sensor
^^^^^^^^^^^^^^^^^
.. autoclass:: ev3devices_ext.GyroSensorExt
    :members:
