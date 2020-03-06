class Pin():
    OUT = 1
    IN = 0

    def __init__(self, pinId, state = 0):
        pass
    
    def value(self, state):
        pass
    
    def high(self):
        pass
    
    def low(self):
        pass

class SPI():
    def __init__(self, spi, baudrate, polarity, phase, bits, firstbit, sck, mosi, miso):
        pass

    def write(self, bytes):
        pass