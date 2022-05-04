import pygame
from random import randint as rando



class EnemyClass:
    xSpeed=0
    ySpeed=0
    maxSpeed=5

    color=( 35, 53, 97)
    points=0
    enemyTime = 0
    width = 20
    height = 20

    image = pygame.image.load('Images/EvilBlob.png')

    def __init__(self,screen,player,BG):
        self.playerObject=player
        self.theScreen=screen
        self.bg = BG

        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]


        self.x = rando(0,self.theScreen.get_size()[0])
        self.y = rando(0,self.theScreen.get_size()[1])


    def enemyDeadTimer(self):
        self.enemyTime +=1

    def update(self,bg):


        self.futureX=self.x+self.xSpeed
        self.futureY=self.y+self.ySpeed


        if self.x+self.width > self.screenWidth:
            self.x = self.screenWidth-self.width
        if self.y+self.height > self.screenHeight:
            self.y = self.screenHeight-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0

        self.pixelColour = bg.get_at((self.futureX, self.futureY))

        if self.pixelColour.r > 100:
            if self.x < self.playerObject.x:
                self.xSpeed = 2
            if self.y < self.playerObject.y:
                self.ySpeed = 2

            if self.x > self.playerObject.x:
                self.xSpeed =- 2
            if self.y > self.playerObject.y:
                self.ySpeed =- 2

            self.x += self.xSpeed
            self.y += self.ySpeed




    def draw(self):
        #pygame.draw.rect(self.theScreen,self.color, pygame.Rect(self.x,self.y, 20,20))
        self.theScreen.blit(self.image, (self.x, self.y))