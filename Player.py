import pygame

class PlayerClass:

    xSpeed=0
    ySpeed=0
    maxSpeed=6
    points=0
    color = (255,0,0)
    backgroundColor = (50, 50, 50)


    def __init__(self,BG,screen,position,PID):
        self.x=position[0]
        self.y=position[1]
        self.width = 20
        self.height = 20
        self.bg = BG
        self.playerID = PID
        self.playerHP = 100

        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]


    def update(self,bg):
        self.futureX=self.x+self.xSpeed
        self.futureY=self.y+self.ySpeed

        self.pixelColour = bg.get_at((self.futureX, self.futureY))

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
        #draw player
        pygame.draw.rect(self.theScreen,self.color, pygame.Rect(self.x,self.y, self.width,self.height))

        #Draw Healthbar
        if self.playerID == 1:
            pygame.draw.rect(self.theScreen, self.backgroundColor, pygame.Rect(self.screenWidth - 200, self.screenHeight- 50, 200, 50))
            # draw points
            pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.screenWidth - 190, self.screenHeight- 45, (self.playerHP * 2) - 20, 40))

        if self.playerID == 2:
            pygame.draw.rect(self.theScreen, self.backgroundColor, pygame.Rect(0, self.screenHeight- 50, 200, 50))
            # draw points
            pygame.draw.rect(self.theScreen, self.color, pygame.Rect(10, self.screenHeight- 45, (self.playerHP * 2) - 20, 40))