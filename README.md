# CircuitPython

# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_Ultrasonic Sensor](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




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
 Final Code for Servo

### Evidence

![Video](https://user-images.githubusercontent.com/90460146/133450204-ae1c807d-1da8-4b4b-83ce-24062d0f11ea.gif)

### Wiring

![Servo Wiring](https://user-images.githubusercontent.com/90460146/133452674-86a69bfd-a632-4746-9df8-652005c39daa.png)


### Reflection

It was difficult at first, I had many problems, but in the end I managed to make it work. The wiring was the main problem. I need to remeber which wire is the power, ground, and analog. I learned that you should color code the wires with the ones coming out of the servo to make it easier for you to wire it up. Black for Black, Red for Red, and White for White.


## CircuitPython_Ultrasonic Sensor

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
New code that I learned for the Ultrasonic Sensor



### Evidence

![Ultrasonic Sensor](https://user-images.githubusercontent.com/90460146/134684198-699c4519-523b-4a43-93d7-e3daae6c354a.gif)



### Wiring

![Sensor Wiring](https://user-images.githubusercontent.com/90460146/134685297-a3c4821e-796a-41b9-bf62-2e5d38b66366.png)


### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
