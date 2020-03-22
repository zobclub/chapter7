from microbit import *
import neopixel

np = neopixel.NeoPixel(pin0, 4)
np.clear()
np.show()
led_on = False

while True:
    if led_on:
        npw = np[3]
        np[3] = np[2]
        np[2] = np[1]
        np[1] = np[0]
        np[0] = npw
        np.show()

    if  button_a.is_pressed():
        led_on = True
        np[0] = (0, 32, 0)
        np[1] = (32, 0, 0)
        np[2] = (0, 0, 32)
        np[3] = (32, 32, 32)
        np.show()

    if  button_b.is_pressed():
        led_on = False
        np.clear()
        np.show()

    sleep(500)