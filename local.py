from canvas import Canvas
import time
from machine import Pin, SPI
from ghost import Ghost
from image import ImageDisplay

BLINKY = (255,0,0)
PINKY = (255, 184, 255)
INKY =  (0, 255, 255)
CLYDE = (255, 184, 82)


canvas = Canvas(16, 16)
ghost = Ghost(BLINKY, 0, 0)
ghost.render(canvas)
image = ImageDisplay()
image.render(canvas)

ghost.set_position((-5,0))
ghost.render(canvas)
image = ImageDisplay()
image.render(canvas)
