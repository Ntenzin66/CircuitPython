import board
import time
import digitalio


pin = digitalio.DigitalInOut(board.D4)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP

    while True:



