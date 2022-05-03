import pygame
from random import randint as rando



class UpgradeClass:

    backgroundColor = (50,50,50)
    color=( 35, 180, 227)



    def __init__(self,screen):

        self.theScreen=screen


        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]

        self.backgroundwidth = 310
        self.backgroundheight = 50
        self.x = (self.screenWidth / 2) - 150
        self.y = 300
        self.points = 0

    def upgradePlayers(self,player1,player2):
        randomupgrade = rando(0,3)
        if randomupgrade == 0:
            player1.maxSpeed += 1
            player2.maxSpeed += 1
        if randomupgrade == 1:
            player1.width += 5
            player1.height += 5
            player2.width += 5
            player2.height += 5
        if randomupgrade == 2:
            player1.width -= 5
            player1.height -= 5
            player2.width -= 5
            player2.height -= 5
        #if randomupgrade == 3:
            #player1.doubleShot = 1
            #player2.DoubleShot = 1



    def update(self,player1,player2):
        self.points += 10

        if self.points > 100:
            self.points -= 100
            self.upgradePlayers(player1,player2)




    def draw(self):
        #Draw background
        pygame.draw.rect(self.theScreen,self.backgroundColor, pygame.Rect(self.x,0,self.backgroundwidth ,self.backgroundheight))
        #draw points
        pygame.draw.rect(self.theScreen, self.color,pygame.Rect(self.x+5, 5, self.points * 3 + 1, 40))