#!/usr/bin/env pybricks-micropython
from fahren import *

# Write your program here
brick.display.clear()

#wait(1000)
#left_motor.set_run_settings(1000,100)
#right_motor.set_run_settings(1000,100)
cmfahren2(1000,100)
wait(1000)
cmfahren2(1000,-100)

