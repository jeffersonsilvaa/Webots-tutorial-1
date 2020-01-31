# **************************************************************
# Project 01 - Disciplina de robótica Móvel UFC / IFCE / LAPISCO
#       Simulação 01 com robô Pioneer 3AT - Webots R2020a
#                   Acionamento dos motores
#        Python 3.6 na IDE Pycharm - controller <extern>
#                By: Jefferson Silva Almeida
#                       Data: 23/01/2020
# **************************************************************

from controller import Robot
from controller import Motor

TIME_STEP = 64
MAX_SPEED = 6.28

# create the robot instance
robot = Robot()

# get a handler to the motors and set target position to infinity (speed control)
leftMotorFront = robot.getMotor('front left wheel')
rightMotorFront = robot.getMotor('front right wheel')
leftMotorBack = robot.getMotor('back left wheel')
rightMotorBack = robot.getMotor('back right wheel')

leftMotorFront.setPosition(float('inf'))
rightMotorFront.setPosition(float('inf'))
leftMotorBack.setPosition(float('inf'))
rightMotorBack.setPosition(float('inf'))

# set up the motor speeds at 10% of the MAX_SPEED.
leftMotorFront.setVelocity(0.1 * MAX_SPEED)
rightMotorFront.setVelocity(0.1 * MAX_SPEED)
leftMotorBack.setVelocity(0.1 * MAX_SPEED)
rightMotorBack.setVelocity(0.1 * MAX_SPEED)


while robot.step(TIME_STEP) != -1:
    pass
