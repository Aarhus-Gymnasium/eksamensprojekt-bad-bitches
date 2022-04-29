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



    def __init__(self,screen,player):
        self.playerObject=player
        self.theScreen=screen


        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]


        self.x = rando(0,self.theScreen.get_size()[0])
        self.y = rando(0,self.theScreen.get_size()[1])


    def enemyDeadTimer(self):
        self.enemyTime +=1

    def update(self):


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
        if self.x < self.playerObject.x:
            self.xSpeed = 1
        if self.y < self.playerObject.y:
            self.ySpeed = 1

        if self.x > self.playerObject.x:
            self.xSpeed =- 1
        if self.y > self.playerObject.y:
            self.ySpeed =- 1



    def draw(self):
        pygame.draw.rect(self.theScreen,self.color, pygame.Rect(self.x,self.y, 20,20))