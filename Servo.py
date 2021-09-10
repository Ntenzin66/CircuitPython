import board
import time
import servo

while True:
    for angle in range(0, 180, 5):
        myServo.angle = 0
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        myServo.angle = 180
        time.sleep(0.05)



