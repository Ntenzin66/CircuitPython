import board
import neopixel
import time
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.Neopixel(board.NEOPIXEL, 1)
dot.brightness = .1



while True:
        try:
            print("sonar.distance")
        except RuntimeError:
            print("Retrying!")
        time.sleep(0.1)

def distance(pos)







