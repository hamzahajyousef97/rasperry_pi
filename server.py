from gcode_reader import arr_angle_of_point
from gcode_reader import arr_angle_of_laser_of_point
from gcode_reader import poly_Num

import RPi.GPIO as GPIO
import time

for i in range(poly_Num):
    angle_point = arr_angle_of_point[i]
    laser_angle = arr_angle_of_laser_of_point[i]
    if angle_point < 0:
        angle_point = 360 + angle_point
        print("negative angle")
    steps_of_rotation = round((float(angle_point) / 360) * 512)
    steps_of_laser = round((float(laser_angle) / 360) * 512)
    GPIO.setmode(GPIO.BOARD)


    control_pins1 = [7,11,13,15]
    for pin in control_pins1:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]
    for i in range(steps_of_rotation):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins1[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
    
    control_pins2 = [12,16,18,22]
    for pin in control_pins2:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]
    for i in range(steps_of_laser):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins2[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

    # GPIO.cleanup()

    input("Do you want to continue")

    control_pins1 = [15,13,11,7]
    for pin in control_pins1:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]
    for i in range(steps_of_rotation):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins1[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)
    
    control_pins2 = [22,18,16,12]
    for pin in control_pins2:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    halfstep_seq = [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1]
    ]
    for i in range(steps_of_laser):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(control_pins2[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.001)

    GPIO.cleanup()















# for i in range(3):
#     input("Enter the value")



# G00 X160.0 Y195.0
# G01 X160.0 Y205.0 
# G02 X140.0 Y205.0 
# G03 X140.0 Y195.0 
# End of polyline


# G00 X160.0 Y-5.0
# G01 X160.0 Y5.0 
# G02 X140.0 Y5.0 
# G03 X140.0 Y-5.0 
# End of polyline
