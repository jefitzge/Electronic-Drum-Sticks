# SOURCE: https://www.techbeamers.com/python-tutorial-write-multithreaded-python-server/
# Used to send data to our server
# SOURCE: https://github.com/adafruit/Adafruit_Python_BNO055
# Used pre-built functions to get data from sensor and make own functions

import sys
import time      
import socket
import logging
import RPi.GPIO as GPIO
from Adafruit_BNO055 import BNO055

# Global variables
global STATE
STATE = False

# Setup button for starting and stopping program
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button to GPIO pin 2

# Setup Server Connection 
host = 'IP_ADDRESS'                                               # address of target/server (IP address of machine running the server) 
port = 2004                                                         # port number of server
BUFFER_SIZE = 20                                                    # size of the buffer holding the message (keep it small to increase speed)
print('Connecting...')
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))
print('connected') 

# Setup connection to BNO055
bno = BNO055.BNO055(serial_port='/dev/serial0', rst=18)
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

# Print BNO055 software revision and other diagnostic data.
sw, bl, accel, mag, gyro = bno.get_revision()
print('Software version:   {0}'.format(sw))
print('Bootloader version: {0}'.format(bl))
print('Accelerometer ID:   0x{0:02X}'.format(accel))
print('Magnetometer ID:    0x{0:02X}'.format(mag))
print('Gyroscope ID:       0x{0:02X}\n'.format(gyro))

print('Reading BNO055 data, press Ctrl-C to quit...')


# This function checks to see if the button has been pressed by the user and changes the value of STATE 
# Allows 
def check_button():
    global STATE
    button_state = GPIO.input(2)
    # Debugging print statement to enusre function is being called
    # print("INSIDE CHECK BUTTON: BUTTON STATE = " + str(button_state)) 
    if (button_state == False): # Button is pressed
        STATE = not STATE
        print("Program started/halted")
        time.sleep(3)
        #print("STATE  = " + str(STATE))
    else:                                                                  # Button was not pressed
        pass                  


# Read the calibration status, modifies existing function call, adds debugging print statements, 
# and retruns a boolen Calibrated True when the system is fully calibrated and false otherwise
# 0=uncalibrated and 3=fully calibrated.
def get_calibration():
    Calibrated = False
    # Get calibration status from BNO055, returns int type
    sys, gyro, accel, mag = bno.get_calibration_status()

    if (gyro >=2 and mag >= 2 and accel >= 2):
        Calibrated = True
    else:
        Calibrated = False

    # We want to see what isnt calibrated so continue to print until all sensors are calibrated
    if (Calibrated == False):
        print("System:{0:0.2F} Gyroscope:{1:0.2F} Accelerometer:{2:0.2F} Magnetometer:{3:0.2F}\n".format(sys, gyro, accel, mag))
    else:
        pass

    return Calibrated

# Modifies pre-exisiting function to add debugging print statements
def get_euler():
    heading, roll, pitch = bno.read_euler()

    # Debugging 
    # print("Roll:{0:0.2F} Pitch:{1:0.2F} Heading:{2:0.2F}".format(roll, pitch, heading))

    return heading, roll, pitch


# This Function takes in a chararacter, corresponding to the drum that is hit, that is then sent to our server via TCP
def play_drum(drum):
    if (drum == "A"):
        tcpClientA.send(bytes('1')) #, 'utf-8'))
        print("SENT: A")
    elif (drum == "B"):
        tcpClientA.send(bytes('2')) #, 'utf-8'))
        print("SENT: B")
    elif (drum == "C"):
        tcpClientA.send(bytes('3')) # , 'utf-8'))
        print("SENT: C")
    elif (drum == "D"):
        tcpClientA.send(bytes('4')) # , 'utf-8'))
        print("SENT: D")
    else:
        print("Error data passed in is formated wrong")

# This Function uses the linear acceleration in the Z direction along with the Roll and Heading of the stick to determine
# which drum is being hit by the user. Values chosen for boundries in relation to the Linear acceleration and Roll can be modified
# to allow for different effects. Making 
def play():
    h, r, p = get_euler()
    x, y, z = bno.read_linear_acceleration()

    # Debugging print statements used to determine if data from sensors are accurate
    # print("Roll:{0:0.2F} Pitch:{1:0.2F} Heading:{2:0.2F}".format(r, p, h))
    # print("Acceleration X:{0:0.2F} Y:{1:0.2F} Z:{2:0.2F}".format(x, y, z))
 
    if(z >= 7):                       
        if(r >= 35 and r <= 40):
            # Debugging print statement
            #print("heading = " + str(h))
            if (h > 0 and h < 45):
                play_drum("A")
            elif(h > 45 and h < 90):
                play_drum("B")
            elif(h > 270 and h < 315):
                play_drum("C")
            elif(h > 315 and h < 360):
                play_drum("D")
            else:
                print("Not a Drum")
        else:
            print("Roll is not in range")
            # Optionally this could be a pass statement, the print is for debugging
    else:
        print("Accleration is not great enough")
        # Optionally this could be a pass statement, the print is for debugging
    


if __name__ == "__main__":
    while True:
        check_button() # should update the value of state
        while (STATE == True):
            c = get_calibration()
            if(c):
                play()
            else:
                pass # print("Not Calibrated")
            check_button()
    GPIO.cleanup()
