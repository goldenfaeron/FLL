#!/usr/bin/env pybricks-micropython
from init import *

def cmfahren(geschwindigkeit,strecke):

   left_motor.reset_angle(0)
   right_motor.reset_angle(0)
   grad=360/(math.pi*wheel_diameter)*strecke*10
   left_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)
   right_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)

   return;

def cmfahren2(geschwindigkeit,strecke):

   left_motor.reset_angle(0)
   right_motor.reset_angle(0)
   grad=360/(math.pi*wheel_diameter)*strecke*10
   left_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)
   right_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)
   while left_motor.angle() <= grad:
      print('works')
      while left_motor.angle() > right_motor.angle():
         print('bigger') 
         wait(5000)
         break
   return;