#!/usr/bin/env pybricks-micropython

import pybricks_ext.ev3brick as brick
from pybricks_ext.ev3devices import Motor, TouchSensor, ColorSensor, GyroSensor, UltrasonicSensor, InfraredSensor
from pybricks_ext.parameters import ColorUtils
from pybricks_ext.speed_util import speed_deg, speed_deg_mm, speed_mm, speed_mm_deg, float_percent, get_ratio
from pybricks_ext.tools import wait, print, StopWatch
from pybricks_ext.ev3brick import display, flashing_lock, light, light_flash, light_pulse, LightFlash, LightPulse, buttons, battery

brick.sound.beep()