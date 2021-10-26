# CircuitPython

# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_UltrasonicSensor](#CircuitPython_UltrasonicSensor)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code

```python
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

dot.brightness = .1

while True:
    dot.fill((255, 0, 255))

```
Above is the code for the Hello Circuitpython assignment. It makes the LED on the metro board turn purple because of the dot.fill((255, 0, 255)) 


### Evidence



https://user-images.githubusercontent.com/90460146/138469157-632eab21-b7bc-462e-b7cf-c8ef22f53c19.mp4

Credit to https://github.com/hheisig51/VigilantWaddle


### Wiring

You do not use wiring in this one, all you do is plug the metro board into the HDMI port on the computer.

### Reflection

It was pretty simple as it was the first assignment. I couldn't really learn arduino that well last year since it was all virtual, so it was  pretty cool learning a new code from scratch.


## CircuitPython_Servo

### Description & Code

```python
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):   # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):  # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```
This is my final code for my Servo. It will rotate to 180 degrees from 0, then from 180 back to 0 at 5 degrees at a time. 

### Evidence

![Video](https://user-images.githubusercontent.com/90460146/133450204-ae1c807d-1da8-4b4b-83ce-24062d0f11ea.gif)

### Wiring

![Servo Wiring](https://user-images.githubusercontent.com/90460146/133452674-86a69bfd-a632-4746-9df8-652005c39daa.png)


### Reflection

It was difficult at first, I had many problems, but in the end I managed to make it work. The wiring was the main problem. I need to remember which wire is the power, ground, and analog. I learned that you should color code the wires with the ones coming out of the servo to make it easier for you to wire it up. Black for Black, Red for Red, and White for White.


## CircuitPython_UltrasonicSensor

### Description & Code

```python
if pos < 5:
        r = 255
        b = 0
        g = 0
    elif pos < 20:
        r = 255-((pos-5)/15*255)
        g = 0
        b = (pos-5)/15*255
    elif pos < 35:
        r = 0
        g = (pos-20)/15*255
        b = 255-((pos-20)/15*255)
    else:
        r = 0
        g = 255
        b = 0

    dot.fill((int(r), int(g), int(b)))

```
Above is the new code that I learned to help me with my Ultrasonic Sensor.


### Evidence

![Ultrasonic Sensor](https://user-images.githubusercontent.com/90460146/134684198-699c4519-523b-4a43-93d7-e3daae6c354a.gif)



### Wiring

![Sensor Wiring](https://user-images.githubusercontent.com/90460146/134685297-a3c4821e-796a-41b9-bf62-2e5d38b66366.png)


### Reflection

This is the hardest but most enjoyable code yet. The first part of printing the distance was pretty simple, but the other half was what I was stuck on for the longest. I managed to get it to change colors from red, to blue, to green, but I could not make it fade. I learned that using equations you can fade colors through the color spectrum. An example of this equation could be, (r = 255-((pos-5)/15*255)



## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
