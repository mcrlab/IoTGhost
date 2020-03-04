from display import Display
import time
from machine import Pin, SPI

WHITE = (255,255,255)
BLACK = (0,0,0)

spi = SPI(2, baudrate=20000000, polarity=0, phase=0, bits=8, firstbit=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
chipSelect = Pin(15, Pin.OUT)
display = Display(16,16, spi, chipSelect)

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

feet = [
    [0,1,1,0,1,1,1,0,0,1,1,1,0,1,1,0],
    [0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

feet2 = [
    [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0],
    [0,0,1,1,0,0,0,1,1,0,0,0,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

def updateCanvas(pixels,x,y, color:
    for rowIndex, row in enumerate(pixels):
        for colIndex, col in enumerate(row):
            if col==1:
                if(rowIndex+y > 15 or colIndex +x > 15):
                    return
                else:
                    display.set_pixel(rowIndex+y, colIndex+x, color)

while True:
    display.fill((0,0,0))
    updateCanvas(body,1,1,(0,0,255))
    updateCanvas(feet,0,13,(0,0,255)
    updateCanvas(eyes,3,4,(0,0,255))
    updateCanvas(mouth,2,10,(127,127,127))
    updateCanvas(pupils,4,6,(127,127,127))

    display.render()

    time.sleep(0.1)

    display.fill((0,0,0))
    updateCanvas(body,1,1,(0,0,255))
    updateCanvas(feet2,0,13,(0,0,255)
    updateCanvas(eyes,3,4,(0,0,255))
    updateCanvas(mouth,2,10,(127,127,127))
    updateCanvas(pupils,4,6,(127,127,127))

    display.render()
    time.sleep(0.1)