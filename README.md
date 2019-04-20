# Electronic-Drum-Sticks
Senior Design Project for Syracuse University.  
### Team
Joseph Fitzgerald Senior CE, Anthony Magari III Senior CE, Aidan Franits Senior EE, and Mark Martello Senior EE.

## Problem Statement
  Traditional, acoustic drum sets contribute to music in most every genre. While their sound is unique and influential, the drums themselves are often physically large, difficult to transport, uncontrollably loud, and expensive. The issues pose numerous challenges for users such as storage, portability, playing without disturbing others, and a significant financial commitment. These issues affect people from school music departments, band members, to the casual drummer.

## Solution
  Our design will help solve these problems by allowing drummers to play with just sticks, no drums. It will allow users to simulate playing traditional drums with 3D printed sticks containing hardware capable of caputring user movement and then sending this information to a server located on a users PC or Laptop to output a sound. Each stick is equiped with a BNO055 IMU Sensor, a Raspberry Pi Zero W, a JuiceBox Zero, a 3.7V Lithium Ion Battery and custom printed PCB to hold all of our components together. Onboard each Raspberry Pi Zero W is a Python program that gathers data from the BNO055 IMU Sensor, interprets this data, and then using a TCP connection sends it to a multi-threaded Python server located on a users PC or Laptop. The server program can read data gathered from the electronic drumsticks and execute audio files via speaker or headphone, at an affordable price.

## How it works
  The first step to play the electronic drums is to run the server code on a PC or Laptop. Have a set of bluetooth headphones or speakers connected to the PC/Laptop to hear the sounds played. To start the electronic drum sticks the user must press the button that is connected to our custom printed PCB. At anytime the user may press this button again to stop the program or hit it to resume playing. After starting the program the user must calibrate the device. The BNO055 offers a variety of sensors in a compact form. These sensors include but are not limted to a Gyroscope, a Magnetometer, and an Accelerometer. To calibrate the Gyroscope the user must leave the sticks flat on a table, or hold them completely still, for a few seconds. To calibrate the Magnetometer the user should move the sensor in a figure 8 motion. To calibrate the Acceleromter the user has to hold the sensor in 6 different orientations, kind of like the sides of a die. This process needs to be repeated for both drum sticks. To locate where the drums are in relation to your sticks you must understand how the drums are created. Using Euler angles given to us by the BNO055 IMU Sensor we can create as many or as few drums as we'd like. For our project we used heading to determine where in space our drums were. Once the BNO055 IMU sensor was calibrated we used 0 heading as our start point. From the start point we subdivided the 180 degrees in front of the user into 4 sections 45 degrees in size. Once we had divied the area in front of the user into 4 distinct sections we needed to choose an angle that would determine where the surface of the drum was in realtion to the stick as it is being swung. We used the roll of the stick to designate the surface of the drum. We then used the linear acceleration of the stick to tell us weather or not the stick was being swung up or down. A user could configure the code to achive a variety of drum sets but for the purpose of our demo we only created 4 drums. 

## Hardware Diagram 
<img src="https://github.com/jefitzge/Electronic-Drum-Sticks/blob/master/Hardware%20Block%20Diagram.PNG" alt="Hardware" width="450" height="450">

*********DESCRIPTION NEEDED*********
## Software Diagram
<img src="https://github.com/jefitzge/Electronic-Drum-Sticks/blob/master/Software%20Block%20Diagram.PNG" alt="Software" width="450" height="150">

*********DESCRIPTION NEEDED*********
## Final Design with 3D Printed Shells
<img src="https://github.com/jefitzge/Electronic-Drum-Sticks/blob/master/Final%20Design.PNG" alt="Final Design" width="350" height="350">

<img src="https://github.com/jefitzge/Electronic-Drum-Sticks/blob/master/Final%20Design%20Closed.PNG" alt="Final Design Closed" width="100" height="250">

### System Demonstration
<a href="https://youtu.be/ExSmOLv3oDM
" target="_blank"><img src="http://img.youtube.com/vi/ExSmOLv3oDM/0.jpg" 
alt="Demonstration" width="240" height="180" border="10" /></a>

This video was taken prior to our Open House demonstration so the Sticks are currently tehtered so that the Lithium Ion Batteries can charge. The design allows users to play without cables attached to the sticks.

## Components and Materials Used
| Component        | Quantity           | Price  | Total Price |
| ------------- |:-------------:| -----:| -----------:|
| Raspberry Pi Zero W      | 2 | $10 | $20 |
| JuiceBox Zero Power Cape | 2 | $34 | $68 |
| Bosh BNO055 IMU Sensor | 2 | $7.95 | $15.90 |
| 3.7V Lithium Ion Battery (2500mAh) | 3 |   $14.95 | $44.85 |
| Printed Circuit Board | 10 | N/A | $15 |
| Miscellaneous | N/A | N/A | $20 |
|  |  |  | **Total Cost: $183.75** |

## Known Issues
- The TCP server needs to be changed to stop it from dropping connection with a stick when it tries to write to a socket in use by another stick.
- The activation zone for the drums needs to be adjusted to more accurately represent a real drum set.

# How to build it
coming soon...
