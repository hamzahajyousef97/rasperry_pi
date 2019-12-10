import sys
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# GPIO24,GPIO25,GPIO8,GPIO7
StepPins1 = [7,11,13,15] # CW rotation
if (sys.argv[2]=="CCW"):
    StepPins1 = [15,13,11,7] # CCW rotation

StepPins2 = [12,16,18,22] # CW rotation
if (sys.argv[4]=="CCW") :
    StepPins2 = [22,18,16,12] # CCW rotation

# Set all pins as output
for pin in StepPins1:
    # print "Setup pins"
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)
for pin in StepPins2:
    # print "Setup pins"
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

# Define some settings
StepCounter = 0
WaitTime = 0.01

# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]

# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]

# Choose a sequence to use
Seq = Seq1
StepCount = StepCount1
Seq = Seq2
StepCount = StepCount2

# Start main loop
steps1 = int(sys.argv[1])
steps2 = int(sys.argv[3])
stepc = 0
while (stepc<=steps1) or (stepc<=steps2):
    if (stepc<=steps1):
        print("Step %i of %i" %(stepc,steps1))
    if (stepc<=steps2):
        print("Step %i of %i" %(stepc,steps2))

for pin in range(0, 4):
    if (stepc<=steps1):
        xpin1 = StepPins1[pin]
        if Seq[StepCounter][pin]!=0:
        # print " Step %i Enable %i" %(StepCounter,xpin1)
            GPIO.output(xpin1, True)
        else:
            GPIO.output(xpin1, False)
    if (stepc<=steps2):
        xpin2 = StepPins2[pin]
        if Seq[StepCounter][pin]!=0:
            # print " Step %i Enable %i" %(StepCounter,xpin2)
            GPIO.output(xpin2, True)
        else:
            GPIO.output(xpin2, False)

StepCounter += 1

# If we reach the end of the sequence
# start again
if (StepCounter==StepCount):
    StepCounter = 0
if (StepCounter<0):
    StepCounter = StepCount

# Wait before moving on
time.sleep(WaitTime)
stepc+=1

GPIO.cleanup()