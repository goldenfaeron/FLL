#!/usr/bin/env pybricks-micropython
from init import *

def cmfahren(geschwindigkeit,strecke):

   left_motor.reset_angle(0)
   right_motor.reset_angle(0)
   grad=360/(math.pi*wheel_diameter)*strecke*10
   print(grad)
   left_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)
   right_motor.run_target(geschwindigkeit, grad)

   return;

def cmfahren2(geschwindigkeit,strecke):

   left_motor.reset_angle(0)
   right_motor.reset_angle(0)
   grad=360/(math.pi*wheel_diameter)*strecke*10
   left_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)
   right_motor.run_target(geschwindigkeit, grad, Stop.COAST, False)
   while abs(left_motor.angle()) <= grad:
      print(abs(left_motor.angle()))
      print(grad)
      if left_motor.speed() > right_motor.speed():
         left_motor.run(right_motor.speed())
         wait(50)
      if left_motor.speed() < right_motor.speed():
         right_motor.run(left_motor.speed())
         wait(50)
   return;