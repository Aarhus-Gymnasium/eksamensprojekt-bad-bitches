import pygame
from random import randint as rando



class UpgradeClass:

    backgroundColor = (50,50,50)
    color=( 35, 180, 227)
    displayPower = 0
    challengeLevel = 1
    powerText = ''
    playerDeadTimerVariable = 0

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
        randomupgrade = rando(0,2)
        if randomupgrade == 0:
            player1.maxSpeed += 1
            player2.maxSpeed += 1
            self.displayPower = 1
            self.powerText = 'Speed Upgrade!'
        if randomupgrade == 1:
            player1.doubleShotPower = True
            player2.doubleShotPower = True
            self.displayPower = 1
            self.powerText = 'Double Shot!'
        if randomupgrade == 2:
            player1.canTeleportPower = True
            player2.canTeleportPower = True
            self.displayPower = 1
            self.powerText = 'Teleport Upgrade!'



    def update(self,player1,player2):
        self.points += 10

        if self.points > 100:
            self.points -= 100
            self.upgradePlayers(player1,player2)
            self.challengeLevel += 1




    def draw(self,font):
        #Draw background
        pygame.draw.rect(self.theScreen,self.backgroundColor, pygame.Rect(self.x,0,self.backgroundwidth ,self.backgroundheight))
        #draw points
        pygame.draw.rect(self.theScreen, self.color,pygame.Rect(self.x+5, 5, self.points * 3 + 1, 40))



        if self.displayPower > 0:
            randomTextColor = ( 35, rando(100,200),  rando(200,255))
            text = font.render(self.powerText, True, randomTextColor)
            text_width, text_height = font.size(self.powerText)
            self.theScreen.blit(text, ((self.screenWidth - text_width) / 2 - rando(-5,5), (self.screenHeight - text_height) / 2 - rando(-5,5)))
            self.displayPower += 1
            if self.displayPower > 120:
                self.displayPower = 0

    def playerIsDead(self,playerObject, surface,font):
        randomTextColor = (35, rando(100, 200), rando(200, 255))
        text = font.render('Player ' + str(playerObject.playerID) + ' is dead!', True, randomTextColor)
        text_width, text_height = font.size('Player ' + str(playerObject.playerID) + 'is dead!')
        surface.blit(text, ((playerObject.screenWidth - text_width) / 2 - rando(-5, 5),
                            (playerObject.screenHeight - text_height) / 2 - rando(-5, 5)))
        self.playerDeadTimerVariable += 1
        if self.playerDeadTimerVariable > 120:
            self.playerDeadTimerVariable = 0

