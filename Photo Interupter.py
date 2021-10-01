import board
import time
import digitalio


pin = digitalio.DigitalInOut(board.D4)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.UP
initial = time.monotonic()

while True:
    now = time.monotonic()
    if now - initial > 4.000:
        print("done")
    else:
        initial = now