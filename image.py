from PIL import Image, ImageDraw
 
img = Image.new('RGB', (10 * 16, 10 * 16), color = 'black')
d = ImageDraw.Draw(img)

d.rectangle((10,10,20,20), fill=(255,0,255))

img.show()