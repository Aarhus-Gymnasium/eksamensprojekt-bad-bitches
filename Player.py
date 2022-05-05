#import random

import pygame
from CircularBufferFile import CircularBuffer
#from controlVariableFile import *




class PlayerClass:

    xSpeed=0
    ySpeed=0
    maxSpeed=6
    points=0

    backgroundColor = (50, 50, 50)
    doubleShotPower = False
    canTeleportPower = False


    def __init__(self,BG,screen,position,PID):
        self.x = position[0]
        self.y=position[1]
        self.width = 20
        self.height = 20
        self.bg = BG


        self.playerID = PID
        if self.playerID == 1:
            self.upVariable = pygame.K_UP
            self.downVariable = pygame.K_DOWN
            self.leftVariable = pygame.K_LEFT
            self.rightVariable = pygame.K_RIGHT
            self.shootVariable = pygame.K_m
            self.teleportVariable = pygame.K_n
            self.color = (255,0,0)
        if self.playerID == 2:

            self.upVariable = pygame.K_w
            self.downVariable = pygame.K_s
            self.leftVariable = pygame.K_a
            self.rightVariable = pygame.K_d
            self.shootVariable = pygame.K_y
            self.teleportVariable = pygame.K_t
            self.color = (0, 0, 255)

        self.playerHP = 100
        self.CircularCordinateBuffer = CircularBuffer(180)  # Class for circular X cord lists for making items follow player


        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]


    def update(self,bg):
        self.CircularCordinateBuffer.enqueue((self.x, self.y))
        if self.CircularCordinateBuffer.is_full():
            self.CircularCordinateBuffer.dequeue()

        self.futureX=self.x+self.xSpeed
        self.futureY=self.y+self.ySpeed




        if self.futureX > 0 and self.futureX < self.screenWidth - self.width:
            self.pixelColour = bg.get_at((self.futureX, self.y))

            if self.pixelColour.r > 100:
                self.x = self.futureX

        if self.futureY > 0 and self.futureY < self.screenHeight-self.height:
            self.pixelColour = bg.get_at((self.x, self.futureY))

            if self.pixelColour.r > 100:
                self.y = self.futureY


    def teleportBack(self):
        if self.canTeleportPower == True:
            self.x, self.y = self.CircularCordinateBuffer.frontOffSet(180)

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

