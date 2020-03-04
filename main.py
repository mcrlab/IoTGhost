from display import Display
import time
from machine import Pin, SPI

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,128)

BLINKY = (255,0,0)
PINKY = (255, 184, 255)
INKY =  (0, 255, 255)
CLYDE = (255, 184, 82)

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
chipSelect = Pin(15, Pin.OUT)
display = Display(16,16, spi, chipSelect)



feet = [
    [0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0],
    [0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


class Ghost():

    body = [
        [0,0,0,0,0,1,1,1,1,1,0,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    eyes = [
        [0,1,1,0,0,0,0,1,1,0],
        [1,1,1,1,0,0,1,1,1,1],
        [1,1,1,1,0,0,1,1,1,1],
        [1,1,1,1,0,0,1,1,1,1],
        [0,1,1,0,0,0,0,1,1,0]

    ]

    pupils = [
        [1,1,0,0,0,0,1,1],
        [1,1,0,0,0,0,1,1]
    ]

    mouth = [
        [0,1,1,0,0,1,1,0,0,1,1,0],
        [1,0,0,1,1,0,0,1,1,0,0,1]
    ]

    feet2 = [
        [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0],
        [0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


    def render(self):
        display.fill((0,0,0))
        color = self.color
        self.updateCanvas(self.body,   1 + self.x, 1 +  self.y, color)
        self.updateCanvas(self.feet2,  0 + self.x, 13 + self.y, color)
        self.updateCanvas(self.eyes,   3 + self.x, 4 +  self.y, WHITE)
        self.updateCanvas(self.mouth,  2 + self.x, 10 + self.y, WHITE)
        self.updateCanvas(self.pupils, 4 + self.x, 6 +  self.y, (0,0,128))

        display.render()

    def updateCanvas(self, pixels, x, y, color):
        for rowIndex, row in enumerate(pixels):
            for colIndex, col in enumerate(row):
                if col==1:
                    if(rowIndex+y > 15 or colIndex +x > 15):
                        return
                    else:
                        display.set_pixel(rowIndex+y, colIndex+x, color)


ghost = Ghost(BLINKY, 0, 0)
ghost.render()