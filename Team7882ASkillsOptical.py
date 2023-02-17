#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
FrontLeft = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
FrontRight = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
optical = Optical(Ports.PORT10)
ConveyorMotor = Motor(Ports.PORT5, GearSetting.RATIO_36_1, False)
StringMotor = Motor(Ports.PORT15, GearSetting.RATIO_36_1, True)
LeftFlywheel = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
RightFlywheel = Motor(Ports.PORT7, GearSetting.RATIO_18_1, True)
string = DigitalOut(brain.three_wire_port.a)
BackLeft = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
BackRight = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project: Competition
#	Authors: Steven Canton
#	Created: Sep 30, 2022
# 
# ------------------------------------------

# Begin project code

# Motor things
Flywheel = MotorGroup(LeftFlywheel, RightFlywheel)
Left = MotorGroup(FrontLeft, BackLeft)
Right = MotorGroup(FrontRight, BackRight)
Conveyor = MotorGroup(ConveyorMotor, StringMotor)

# Port 1 FrontLeft, Green, Reverse
# Port 2 FrontRight, Green, Normal
# Port 3 BackLeft, Green, Reverse
# Port 8 BackRight, Green, Normal
# Port 5 ConveyorMotor, Red, Reverse
# Port 6 LeftFlywheel, Green, Normal
# Port 7 RightFlywheel, Green, Reverse
# Port 15 StringMotor, Red, Reverse
# Port 10 optical

def autonomous():
    '''

    THIS IS A MANUAL, PLEASE READ BEFORE PROGRAMMING AUTONOMOUS
    Use MoveForward() MoveBack() TurnLeft() and TurnRight() to move the robot easier. 
    Inside the parentheses input the amount of time (in seconds) you want the robot 
    to move or turn in the respective direction. You also need to put in the amount of
    volts that will go to the motors when the function is called. 

    For MoveForward() there is a parameter that allows you to use the conveyor whilst you move.
    Input either True or False into this area to say if the conveyor should move.

    There is also ConveyorSpin() and FlywheelSpin() which ConveyorSpin() only has time as a 
    parameter, whilst FlywheelSPin has both the time and the volts.

    There is also OpticalChecker(), which is the roller spinner. I could defo change the name.
    It has no parameters but is currently not able to use

    Also, StringStart() and StringEnd() have no parameters and dont have any wait functions,
    so you can make it drop the string while moving the robot. 

    ShootDisk() moves all of the conveyor motors as well as the Flywheels, its used as a general
    function when you want to have the disks to shoot.
    It only uses one parameter, which is the amount of time you want the motors to move.

    RotateForward() and RotateReverse() are functions that take in a number and a list for the
    all of the motors you want to rotate in the respective direction of the function.
    The number that you input is the amount of seconds you want those motors to rotate.

    Zero volts does nothing and 12 volts go the fastest that the motor can move

    The fuctions should be like this:

    MoveForward([the amount of seconds you want], [volts from 0 - 12], [If you would like]
                                                                [the cnoveyor to go while moving]) 
    MoveBack([seconds], [volts]) 
    TurnLeft([seconds], [volts])
    TurnRight([seconds], [volts])
    ConveyorSpin([seconds], [volts], [direction])
    FlywheelSpin([seconds], [volts])
    OpticalChecker()
    StringStart()
    StringEnd()
    ShootDisk([seconds])
    RotateForward([seconds], [list of motors])
    RotateReverse([seconds], [list of motors])

    Note that autonomous is only 15 seconds, so be mindfull of how much time you spend using the functions
    '''

    def CarsonSkills():

        # Get the roller and turn right towards the high goa closest to us
        SkillsOpticalChecker()
        MoveForward(.3, 6)

        # 90 degree turn to the right towards the high goal
        TurnRight(.5,6)

        MoveForward(1,6)
        TurnLeft(.2,6)

        # Shoot disks into high goal
        ShootDisk(5,12)

        # Go into low goa to avoid other disks
        TurnRight(.2,6)
        MoveForward(.5,6)

        # Turn inside the low goal towards the other roller (Turned so we move backwards)
        TurnRight(.5,6)
        MoveBack(2,6)

        # Get the low goal
        TurnRight(.5,6)
        SkillsOpticalChecker()

        # Now we get the disk, and then turn back around to get the other roller
        MoveBack(.3,6)
        TurnRight(.3,6)
        MoveForward(.5,6)
        ConveyorSpin(2,12)

        # Get roller
        TurnLeft(.7)
        MoveBack(.3,6)
        SkillsOpticalChecker()

        # At this point we restart the code to do the same thing on the opposite side, well keep the comments

        # Get the roller and turn right towards the high goa closest to us
        SkillsOpticalChecker()
        MoveForward(.3, 6)

        # 90 degree turn to the right towards the high goal
        TurnRight(.5,6)

        MoveForward(1,6)
        TurnLeft(.2,6)

        # Shoot disks into high goal
        ShootDisk(5,12)

        # Go into low goa to avoid other disks
        TurnRight(.2,6)
        MoveForward(.5,6)

        # Turn inside the low goal towards the other roller (Turned so we move backwards)
        TurnRight(.5,6)
        MoveBack(2,6)

        # Get the low goal
        TurnRight(.5,6)
        SkillsOpticalChecker()

        # Now because we already have the other roller well actiate strings since its the end
        String()

    def skills(): # A little Tested

        # First Roller
        MoveBack(.2,6)
        SkillsOpticalChecker()
        MoveForward(.2, 6)
        wait(.2, SECONDS)
        TurnLeft(.4, 6)
        wait(.2,SECONDS)
        MoveForward(.7, 6, True)
        wait(.2,SECONDS)
        ConveyorSpin(.5, 12, FORWARD)
        wait(.2,SECONDS)
        TurnRight(1, 6)
        wait(.2,SECONDS)
        MoveBack(.9, 6)
        wait(.2, SECONDS)

        # Second Roller
        SkillsOpticalChecker()
        MoveForward(.3, 6)
        wait(.2,SECONDS)
        TurnLeft(.85, 6)
        wait(.2,SECONDS)
        MoveForward(1, 6)
        wait(.2,SECONDS)
        ConveyorSpin(.7,12,REVERSE)
        ShootDisk(7,9.5)

        TurnRight(.9, 6)
        wait(.2,SECONDS)
        MoveForward(.5,6)

        # Change to backward
        # MoveBack(4, 6, True)
        # wait(.2,SECONDS)

        # # Turn and shoots disks at the high goal
        # MoveForward(2, 6)
        # wait(.2,SECONDS)
        # TurnRight(1.2, 6)
        # wait(.2,SECONDS)
        # MoveBack(.4, 6)

        # # Start of second side (Third Roller)
        # SkillsOpticalChecker()
        # MoveForward(.3, 6)
        # wait(.2,SECONDS)
        # TurnLeft(.4, 6)
        # wait(.2,SECONDS)
        # MoveForward(1.1, 6, True)
        # wait(.2,SECONDS)
        # TurnRight(1.2, 6)
        # wait(.2,SECONDS)
        # MoveBack(.4, 6)

        # # Fourth Roller
        # SkillsOpticalChecker()
        # MoveForward(.3, 6)
        # wait(.2,SECONDS)
        # TurnLeft(.4, 6)
        # wait(.2,SECONDS)
        # MoveForward(2, 6, True)

        # # Turns and shoots at high goal again
        # TurnLeft(.5, 6)
        # wait(.2,SECONDS)
        # ShootDisk(3)
        # wait(.2,SECONDS)

        # Since we are already turned towards teh high goal, we can see how the strings shoot when we are pointed at it
        String()

    #Start of Functions for Autonomous
    def MoveForward(timeF, WheelSpeed = 12, inp = False):
        Left.spin(FORWARD, WheelSpeed, VOLT)
        Right.spin(FORWARD, WheelSpeed, VOLT)

        if inp == True:
            Conveyor.spin(FORWARD, 12, VOLT)
    
        wait(timeF, SECONDS)

        if inp == True:
            Conveyor.stop()

        Left.stop()
        Right.stop()


    def MoveBack(timeB, WheelSpeed = 12):
        Left.spin(REVERSE, WheelSpeed , VOLT)
        Right.spin(REVERSE, WheelSpeed, VOLT)
        wait(timeB, SECONDS)
        Left.stop()
        Right.stop()

    def TurnLeft(timeL, WheelSpeed = 12):
        Left.spin(REVERSE, WheelSpeed, VOLT)
        Right.spin(FORWARD, WheelSpeed, VOLT)
        wait(timeL, SECONDS)
        Left.stop()
        Right.stop()

    def TurnRight(timeR, WheelSpeed = 12):
        Left.spin(FORWARD, WheelSpeed, VOLT)
        Right.spin(REVERSE, WheelSpeed, VOLT)
        wait(timeR, SECONDS)
        Left.stop()
        Right.stop()

    def ConveyorSpin(timeV, ConveyorSpeed = 12, forr = FORWARD):
        Conveyor.spin(forr, ConveyorSpeed, VOLT)
        wait(timeV, SECONDS)
        Conveyor.stop()

    def FlywheelSpin(timeG, GS = 12):
        Flywheel.spin(FORWARD, GS, VOLT)
        wait(timeG, SECONDS)
        Flywheel.stop()

    def ShootDisk(timeD, AllSpeed = 12):
        Conveyor.spin(FORWARD, 12, VOLT)
        Flywheel.spin(FORWARD, AllSpeed, VOLT)
        wait(timeD, SECONDS)
        Conveyor.stop()
        Flywheel.stop()

    def SkillsOpticalChecker():
        optical.set_light(LedStateType.ON)
        optical.set_light_power(25, PERCENT)

        notwanted = Color.BLUE
        wanted = Color.RED

        Conveyor.spin(FORWARD, 8, VOLT)
        wait(.3,SECONDS)
        Conveyor.stop()

        Left.spin(REVERSE, 4, VOLT)
        Right.spin(REVERSE, 4, VOLT)
        wait(.2,SECONDS)
        Left.stop()
        Right.stop()

        for _ in range(100):
            Conveyor.spin(REVERSE, 10, VOLT)

            if optical.color() == notwanted:
                pass
            
            elif optical.color() == wanted:
                wait(.18, SECONDS)
                Conveyor.stop()
                optical.set_light(LedStateType.OFF)
                Left.stop()
                Right.stop()
                controller_1.screen.print("Red found")
                break

    def String():
        string.set(True)
        wait(.5,SECONDS)
        string.set(False)

    def RotateForward(sec, motors):
        for motor in motors:
            motor.spin(FORWARD)
        wait(sec, SECONDS)
        for motor in motors:
            motor.stop()

    def RotateReverse(sec, motors):
        for motor in motors:
            motor.spin(REVERSE)
        wait(sec, SECONDS)
        for motor in motors:
            motor.stop()

    # End of autonomous functions

    wait(.3,SECONDS)

    skills()


def pre_autonomous():

    #Print port setings so that team can seamlessly know where each motor is connected
    brain.screen.print("Front Left Wheel: 1 Back: 3")
    brain.screen.next_row()
    brain.screen.print("Front Right Wheel: 2 Back: 4")
    brain.screen.next_row()
    brain.screen.print("Conveyor System: 5")
    brain.screen.next_row()
    brain.screen.print("Left Flywheel: 6")
    brain.screen.next_row()
    brain.screen.print("Right Flywheel: 7")
    brain.screen.next_row()
    brain.screen.print("Optical: 11")
    brain.screen.next_row()
    brain.screen.print("The string launchers: A")
    brain.screen.next_row()
    brain.screen.print("The string motors: 15")

    #Set velocities
    Left.set_velocity(85,PERCENT)
    Right.set_velocity(85,PERCENT)
    Flywheel.set_velocity(100,PERCENT)
    Conveyor.set_velocity(100,PERCENT)
    StringMotor.set_velocity(100,PERCENT)
    Conveyor.set_max_torque(100,PERCENT)

    #Variables
    FlywheelSpeed = 12.0
    intakeIn = False
    intakeOut = False

    #Setting motors to their respective stopping positions
    Left.set_stopping(BRAKE)
    Right.set_stopping(BRAKE)
    Flywheel.set_stopping(BRAKE)
    Conveyor.set_stopping(BRAKE)
    StringMotor.set_stopping(BRAKE)

    #Function for controller printing
    def printing(num):
        controller_1.screen.clear_screen()
        controller_1.screen.set_cursor(1,1)
        controller_1.screen.print("Flywheel speed: ")
        controller_1.screen.set_cursor(1,16)
        controller_1.screen.print(num)

    #Functions For Controller Inputs:
    #Robot Movement (Axis 2 and 3)
    def Axis3Changed():
        Left.spin(FORWARD, controller_1.axis3.position(), VOLT)

    def Axis2Changed():
        Right.spin(FORWARD, controller_1.axis2.position(), VOLT)

    #Conveyor (Button B)
    def ButtonBPressed():
        Conveyor.spin(FORWARD)
    def ButtonBReleased():
        Conveyor.stop()
    #Flywheel (Button A)
    def ButtonAPressed():
        Flywheel.spin(FORWARD, FlywheelSpeed, VOLT)

    def ButtonAReleased():
        Flywheel.stop()

    #Changing the Speed of the Flywheel (L2 and R2) and making the flwheel go as well
    def LeftB2():
        global FlywheelSpeed
        if FlywheelSpeed < 12.0:
            FlywheelSpeed += 1.0
        Flywheel.spin(FORWARD, FlywheelSpeed, VOLT)
        printing(FlywheelSpeed)

    def LeftB2R():
        Flywheel.stop()

    def RightB2():
        global FlywheelSpeed
        if FlywheelSpeed > 0:
            FlywheelSpeed -= 1.0
        Flywheel.spin(FORWARD, FlywheelSpeed, VOLT)
        printing(FlywheelSpeed)

    def RightB2R():
        Flywheel.stop()

    #Endgame string launching
    def LeftB1P():
        Conveyor.spin(REVERSE)

    def LeftB1R():
        # if intakeOut == False:
        #     intakeOut = True
        # elif intakeOut == True:
        #     intakeOut = False
        Conveyor.stop()

    def RightB1P():    
        Conveyor.spin(FORWARD)

    def RightB1R():
        # if intakeIn == False:
        #     intakeIn = True
        # elif intakeIn == True:
        #     intakeIn = False
        Conveyor.stop()

    def ButtonDownPressed():
        StringMotor.spin(REVERSE)

    def ButtonDownReleased():
        StringMotor.stop()

    def ButtonUpPressed():
        StringMotor.spin(FORWARD)

    def ButtonUpReleased():
        StringMotor.stop()
    # system event handlers
    controller_1.axis3.changed(Axis3Changed)
    controller_1.axis2.changed(Axis2Changed)
    controller_1.buttonB.pressed(ButtonBPressed)
    controller_1.buttonA.pressed(ButtonAPressed)
    controller_1.buttonB.released(ButtonBReleased)
    controller_1.buttonA.released(ButtonAReleased)
    controller_1.buttonL2.pressed(LeftB2)
    controller_1.buttonR2.pressed(RightB2)
    controller_1.buttonL2.released(LeftB2R)
    controller_1.buttonR2.released(RightB2R)
    controller_1.buttonL1.pressed(LeftB1P)
    controller_1.buttonL1.released(LeftB1R)
    controller_1.buttonR1.pressed(RightB1P)
    controller_1.buttonR1.released(RightB1R)
    controller_1.buttonDown.pressed(ButtonDownPressed)
    controller_1.buttonDown.released(ButtonDownReleased)
    controller_1.buttonUp.pressed(ButtonUpPressed)
    controller_1.buttonUp.released(ButtonUpReleased)
    controller_1.buttonX.released(autonomous)

    # add 15ms delay to make sure events are registered correctly.
    wait(15, MSEC)

def user_control():
    pass

#create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()

