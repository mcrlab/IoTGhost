from canvas import Canvas
import time
from machine import Pin, SPI
from ghost import Ghost
from unicorn import UnicornHat

BLINKY = (255,0,0)
PINKY = (127, 92, 127)
INKY =  (0, 127, 127)
CLYDE = (127, 92, 41)

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
chipSelect = Pin(15, Pin.OUT)

canvas = Canvas(16, 16)
ghost = Ghost(PINKY, 0, 0)
ghost.set_direction((0,-1))
x = 0

while True:
    ghost.render(canvas)
    image = UnicornHat(spi, chipSelect)
    image.render(canvas)


    time.sleep(0.1)