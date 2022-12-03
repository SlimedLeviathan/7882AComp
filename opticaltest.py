def OpticalChecker():
    optical.set_light(LedStateType.ON)
    optical.set_light_power(25, PERCENT)

    colorFound = False
    while colorFound == False:
        if optical.color() == Color.RED:
            colorFound = True
            ogColor = Color.BLUE
            opColor = Color.RED
            controller_1.screen.print("Red")
    
        elif optical.color() == Color.BLUE:
            colorFound = True
            ogColor = Color.RED
            opColor = Color.BLUE
            controller_1.screen.print("Blue")
            
    done = False
    if done == False:
        if optical.color() == ogColor:
            Conveyor.spin(FORWARD)
        elif optical.color() == opColor:
            wait(.5, SECONDS)
            done = True
            Conveyor.stop()
