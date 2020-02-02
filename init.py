from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math

#from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
#robot2 = MoveTank(left_motor, right_motor)
wheel_diameter = 54
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

