import pygame
from random import randint as rando


#This class controls upgrades, and the text that appears on screen.
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

    def upgradePlayers(self,player,randomupgrade):
        #This code upgrades the players speed, and fixes a drift that would happen when you upgraded before.
        #This code is adapted from https://github.com/Farpeja02/theGame/commit/faee157b0bd59ed1caf608528677f0b4b5225766 from the changeSpeedToFixed method.
        if randomupgrade == 0:
            player.maxSpeed += 1
            if player.xSpeed > 0:
                player.xSpeed = player.maxSpeed
            elif player.xSpeed < 0:
                player.xSpeed = (-1) * player.maxSpeed
            if player.ySpeed > 0:
                player.ySpeed = player.maxSpeed
            elif player.ySpeed < 0:
                player.ySpeed = (-1) * player.maxSpeed
            self.displayPower = 1
            self.powerText = 'Speed Upgrade!'
        if randomupgrade == 1:
            player.doubleShotPower = True
            self.displayPower = 1
            self.powerText = 'Double Shot!'
        if randomupgrade == 2:
            player.canTeleportPower = True
            self.displayPower = 1
            self.powerText = 'Teleport Upgrade!'


    #This update is run when an enemy is killed, and runs upgrade players if at 100 points.
    def update(self):
        self.points += 20
        if self.points > 100:
            self.points -= 100
            self.challengeLevel += 1
            return True
        else:
            return False




    def draw(self,font):
        #Draw background
        pygame.draw.rect(self.theScreen,self.backgroundColor, pygame.Rect(self.x,0,self.backgroundwidth ,self.backgroundheight))
        #draw points
        pygame.draw.rect(self.theScreen, self.color,pygame.Rect(self.x+5, 5, self.points * 3 + 1, 40))


        #This draws the nexest upgrade gotten for 2 seconds.
        if self.displayPower > 0:
            randomTextColor = ( 35, rando(100,200),  rando(200,255))
            text = font.render(self.powerText, True, randomTextColor)
            text_width, text_height = font.size(self.powerText)
            self.theScreen.blit(text, ((self.screenWidth - text_width) / 2 - rando(-5,5), (self.screenHeight - text_height) / 2 - rando(-5,5)))
            self.displayPower += 1
            if self.displayPower > 120:
                self.displayPower = 0

    #If a player dies, it draws which player, and adds it to the screen.
    #It checks how wide and high the text is, and makes sure it is in the middle no matter what.
    def playerIsDead(self,playerObject, surface,font):
        randomTextColor = (rando(200,230), rando(50, 100), 0)
        text = font.render('Player ' + str(playerObject.playerID) + ' is dead!', True, randomTextColor)
        text_width, text_height = font.size('Player ' + str(playerObject.playerID) + 'is dead!')
        surface.blit(text, ((playerObject.screenWidth - text_width) / 2 - rando(-5, 5),
                            (playerObject.screenHeight - text_height) / 2  - 300- rando(-5, 5)))
        self.playerDeadTimerVariable += 1
        if self.playerDeadTimerVariable > 120:
            self.playerDeadTimerVariable = 0

