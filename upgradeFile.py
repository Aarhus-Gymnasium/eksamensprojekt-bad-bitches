import pygame
from random import randint as rando



class UpgradeClass:

    backgroundColor = (50,50,50)
    color=( 35, 180, 227)
    displayDoubleUpgrade = 0
    displayTeleportPower = 0
    challengeLevel = 1


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
        randomupgrade = rando(0,4)
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
        if randomupgrade == 3:
            player1.doubleShotPower = True
            player2.doubleShotPower = True
            self.displayDoubleUpgrade = 1
        if randomupgrade == 4:
            player1.canTeleportPower = True
            player2.canTeleportPower = True
            self.displayTeleportPower = 1



    def update(self,player1,player2):
        self.points += 50

        if self.points > 100:
            self.points -= 100
            self.upgradePlayers(player1,player2)
            self.challengeLevel += 1




    def draw(self,font):
        #Draw background
        pygame.draw.rect(self.theScreen,self.backgroundColor, pygame.Rect(self.x,0,self.backgroundwidth ,self.backgroundheight))
        #draw points
        pygame.draw.rect(self.theScreen, self.color,pygame.Rect(self.x+5, 5, self.points * 3 + 1, 40))

        if self.displayDoubleUpgrade > 0:
            randomTextColor = ( 35, rando(100,200),  rando(200,255))
            text = font.render('Double SHOT!', True, randomTextColor)
            self.theScreen.blit(text, ( rando(52,67), (self.screenHeight / 2) - rando(92,108)))
            self.displayDoubleUpgrade += 1
            if self.displayDoubleUpgrade > 120:
                self.displayDoubleUpgrade = 0


        if self.displayTeleportPower > 0:
            randomTextColor = ( 35, rando(100,200),  rando(200,255))
            text = font.render('Teleport!', True, randomTextColor)
            self.theScreen.blit(text, ( rando(232,247), (self.screenHeight / 2) - rando(92,108)))
            self.displayTeleportPower += 1
            if self.displayTeleportPower > 120:
                self.displayTeleportPower = 0

