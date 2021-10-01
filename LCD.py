import board
import touchio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = board.I2C()

touch_pad = board.A1  # Will not work for Circuit Playground Express!
# touch_pad = board.A1  # For Circuit Playground Express
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
touch = touchio.TouchIn(touch_pad)

counter = 0
sky1 = 0
ske2 = 0

while True:
    if touch.A1.value: and sky1 = 1:
        counter += 1
        lcd.home()
        lcd.clear()
        lcd.print("Touched!")
    else:
        lcd.home()
        lcd.print("No Touchie!")
        time.sleep(0.5)