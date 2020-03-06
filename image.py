from PIL import Image, ImageDraw
from canvas import Canvas

class ImageDisplay():
    def __init__(self):
        pass

    def render(self, canvas):
        width = canvas.width
        height = canvas.height
        
        data = canvas.get_buffer();
        img = Image.new('RGB', (width * 10, height * 10), color = (0, 0, 0))
        draw = ImageDraw.Draw(img)
        i = 0

        while(i < len(data)):
            r = data[i]
            g = data[i + 1]
            b = data[i + 2]
            
            m = i / 3

            y = ((m - (m % width)) / width) * 10

            x = (m % width) * 10
            draw.rectangle((x,y,x+10,y + 10), fill=(r,g,b))


            i = i + 3


        img.show()

