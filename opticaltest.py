#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
optical = Optical(Ports.PORT4)
funkymotor = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

# while True:
#     if optical.color() == Color.RED:
#         brain.screen.set_cursor(1,1)
#         brain.screen.print("REDD")
#         funkymotor.spin(REVERSE)
#     elif optical.color() == Color.BLUE:
#         brain.screen.set_cursor(1,1)
#         brain.screen.print("BLUE")
#         funkymotor.spin(FORWARD)
#     else:
#         brain.screen.set_cursor(1,1)
#         brain.screen.print("NOPE")
#         funkymotor.stop()

optical.set_light(LedStateType.ON)
optical.set_light_power(25, PERCENT)

colorFound = False
while colorFound == False:
    if optical.color() == Color.RED:
        colorFound = True
        ogColor = Color.RED
        opColor = Color.BLUE
        brain.screen.print("Red")
    
    elif optical.color() == Color.BLUE:
        colorFound = True
        ogColor = Color.BLUE
        opColor = Color.RED
        brain.screen.print("Blue")

done = False
while done == False:
    if optical.color() == ogColor:
        funkymotor.spin(FORWARD)
    elif optical.color() == opColor:
        wait(.3,SECONDS)
        funkymotor.stop()
        done= True