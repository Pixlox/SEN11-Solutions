from microbit import *
import music

maxTiltAllowed = 150
tiltCount = 0
checking = False

def isFlat():
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    return x > -maxTiltAllowed and x < maxTiltAllowed and y > -maxTiltAllowed and y < maxTiltAllowed

while True:
    if button_a.was_pressed():
        checking = True
        tiltCount = 0
        display.scroll("GO")

    if checking:
        if not isFlat():
            tiltCount += 1
            set_volume(255)
            music.play(music.BA_DING)

    if button_b.was_pressed():
        checking = False
        display.scroll(tiltCount)
