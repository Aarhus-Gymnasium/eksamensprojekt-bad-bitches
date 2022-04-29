import pygame

class PlayerClass:

    xSpeed=0
    ySpeed=0
    maxSpeed=6
    points=0
    color = (255,0,0)

    def __init__(self,BG,screen,xpos,ypos):
        self.x=xpos
        self.y=ypos
        self.width = 20
        self.height = 20
        self.bg = BG

        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]


    def update(self):
        self.futureX=self.x+self.xSpeed
        self.futureY=self.y+self.ySpeed

        self.pixelColour = self.bg.get_at((self.futureX, self.futureY))

        if self.pixelColour.r > 100:
            self.x = self.futureX

            self.y = self.futureY


        #safety to prevent overshoot:
        if self.x+self.width > self.screenWidth:
            self.x = self.screenWidth-self.width
        if self.y+self.height > self.screenHeight:
            self.y = self.screenHeight-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0


    def draw(self):
        pygame.draw.rect(self.theScreen,self.color, pygame.Rect(self.x,self.y, 20,20))