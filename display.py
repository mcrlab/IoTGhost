
_SOF = 0x72

class Display:

    def __init__(self, width, height, spi, chipSelect):
        self.width = width
        self.height = height
        self.buffer = [0] * ((x * y) * 3)
        self.spi = spi 
        self.cs = chipSelect 

    def fill(self, color):
        r, g, b = color
        bufferSize = len(self.buffer)
        i = 0
        while(i < bufferSize):
            self.buffer[i]     = r
            self.buffer[i + 1] = g
            self.buffer[i + 2] = b
            i = i + 3

    def clear(self):
        self.fill(0,0,0)

    def off(self):
        self.fill(0,0,0)
        self.render()

    def set_pixel(self, x, y, color):
        r, g, b = color
        position = ((y * self.x) + x) * 3
        self.buffer[position]     = r
        self.buffer[position + 1] = g
        self.buffer[position + 2] = b

    def render(self):
        self.cs.value(0)
        self.spi.write(bytes([_SOF] + self.buffer))
        self.cs.value(1)