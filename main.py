#!/usr/bin/env pybricks-micropython
from fahren import *

# Write your program here
print ("Test")
brick.display.clear()

#wait(1000)
left_motor.set_run_settings(1000,100)
right_motor.set_run_settings(1000,100)
cmfahren2(100,500)
wait(1000)
cmfahren2(100,-500)

