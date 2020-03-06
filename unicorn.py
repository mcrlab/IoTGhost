class UnicornHat():
    _SOF = 0x72

    def __init__(self, spi, chipSelect):
        self.spi = spi
        self.cs = chipSelect
    
    def render(self, canvas):
        self.cs.value(0)
        self.spi.write(bytes([self._SOF] + canvas.get_buffer()))
        self.cs.value(1)