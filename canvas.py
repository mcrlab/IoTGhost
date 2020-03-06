
class Canvas:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [0] * ((width * height) * 3)


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
        self.fill((0,0,0))


    def set_pixel(self, x, y, color):

        if x >= self.width or y >= self.height or x < 0 or y < 0:
            return

        r, g, b = color
        position = ((y * self.width) + x) * 3
        self.buffer[position]     = r
        self.buffer[position + 1] = g
        self.buffer[position + 2] = b

    def get_buffer(self):
        return self.buffer
        