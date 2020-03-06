WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,128)


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

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.direction = (0,0)
        self.frame0 = True
        self.edible = False

    def set_color(self, color):
        self.color = color

    def set_position(self, position=(0,0)):
        self.x, self.y = position
    
    def set_direction(self, direction = (0,0)):
        self.direction = direction

    def render(self, canvas):
        canvas.fill(BLACK)
        color = self.color
        directionX, directionY = self.direction
        
        self.x = self.x + directionX
        self.y = self.y + directionY

        if self.x <= -16:
            self.x = 16
        elif self.x > 16:
            self.x = -16

        if self.y <= -16:
            self.y = 16
        elif self.y > 16:
            self.y = -16
            

        self.updateCanvas(canvas, self.body,   1 + self.x, 1 +  self.y, color)
        self.updateCanvas(canvas, self.eyes,   3 + self.x, 4 +  self.y, WHITE)
        self.updateCanvas(canvas, self.pupils, 4 + self.x, 6 +  self.y, (0,0,128))
        
        #self.updateCanvas(canvas, self.mouth,  2 + self.x, 10 + self.y, WHITE)
        

        if(self.frame0):
            self.updateCanvas(canvas, self.feet2,  0 + self.x, 13 + self.y, color)
            self.frame0 = False
        else:
            self.updateCanvas(canvas, self.feet,  0 + self.x, 13 + self.y, color)
            self.frame0 = True

    def updateCanvas(self,canvas, pixels, x, y, color):
        for rowIndex, row in enumerate(pixels):
            for colIndex, col in enumerate(row):
                if col==1:
                    canvas.set_pixel(colIndex+x, rowIndex+y, color)