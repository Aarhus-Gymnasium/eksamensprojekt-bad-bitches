import random
import numpy as np
import NoiseMapFile as NMF
from Player import PlayerClass
from Enemy import EnemyClass
#from Shot import ShotClass
from upgradeFile import UpgradeClass
import pygame
from Shot import ShotClass
#from keyboardControlFunctionFile import movementfunction


pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 110)


clock = pygame.time.Clock()
gameWindowHeight=1024
gameWindowWidth=1024

enemies=[]
shots = []
players = []


def movementfunction(event):
    for playerObject in players:
        if event.type == pygame.KEYDOWN:
            if event.key == playerObject.playerMovement["upVariable"]:
                playerObject.ySpeed -= playerObject.maxSpeed
            if event.key == playerObject.playerMovement["downVariable"]:
                playerObject.ySpeed += playerObject.maxSpeed
            if event.key == playerObject.playerMovement["leftVariable"]:
                playerObject.xSpeed -= playerObject.maxSpeed
            if event.key == playerObject.playerMovement["rightVariable"]:
                playerObject.xSpeed += playerObject.maxSpeed



            if event.key == playerObject.playerMovement["shootVariable"]:
                shots.append(ShotClass(screen, spawnPosX=playerObject.x + playerObject.width / 2,
                                       spawnPosY=playerObject.y + playerObject.height / 2, playerSpeedX=playerObject.xSpeed,
                                       playerSpeedY=playerObject.ySpeed))
                if playerObject.doubleShotPower == True:
                    shots.append(ShotClass(screen, spawnPosX=playerObject.x + playerObject.width / 2,
                                           spawnPosY=playerObject.y + playerObject.height / 2,
                                           playerSpeedX=playerObject.xSpeed - (playerObject.ySpeed / 2),
                                           playerSpeedY=playerObject.ySpeed + (playerObject.xSpeed / 2)))
                    shots.append(ShotClass(screen, spawnPosX=playerObject.x + playerObject.width / 2,
                                           spawnPosY=playerObject.y + playerObject.height / 2,
                                           playerSpeedX=playerObject.xSpeed + (playerObject.ySpeed / 2),
                                           playerSpeedY=playerObject.ySpeed - (playerObject.xSpeed / 2)))
            if event.key == playerObject.playerMovement["teleportVariable"]:
                playerObject.teleportBack()

        if event.type == pygame.KEYUP:
            if event.key == playerObject.playerMovement["upVariable"]:
                playerObject.ySpeed += playerObject.maxSpeed
            if event.key ==playerObject.playerMovement["downVariable"]:
                playerObject.ySpeed -= playerObject.maxSpeed
            if event.key == playerObject.playerMovement["leftVariable"]:
                playerObject.xSpeed += playerObject.maxSpeed
            if event.key == playerObject.playerMovement["rightVariable"]:
                playerObject.xSpeed -= playerObject.maxSpeed
def generateEnemy():
    i = False
    while i == False:
        enemyXRandomVal = random.randint(1, gameWindowWidth - 1)
        enemyYRandomVal = random.randint(1, gameWindowHeight - 1)
        if abs(enemyXRandomVal - playerObject1.x and playerObject2.x) > 100 and abs(enemyYRandomVal - playerObject1.y and playerObject2.y > 100):
            pixelColour = backGroundIMG.get_at((enemyXRandomVal, enemyYRandomVal))
            if pixelColour.r == 255:
                i = True
                whoToTarget = random.randint(0, 1)
                if whoToTarget == 0:
                    enemy = EnemyClass(screen=screen, player=playerObject1, BG=backGroundIMG,X=enemyXRandomVal,Y=enemyYRandomVal)
                else:
                    enemy = EnemyClass(screen=screen, player=playerObject2, BG=backGroundIMG,X=enemyXRandomVal,Y=enemyYRandomVal)
                enemies.append(enemy)
def invertMap():
    temp = pygame.surfarray.array2d(backGroundIMG)
    blank = np.full((gameWindowWidth, gameWindowHeight), 255)
    inverted = blank - temp
    surface = pygame.surfarray.make_surface(inverted)
    return surface
def findSpawnForPlayer():
    i = False
    playerXRandomVal = random.randint(20, gameWindowWidth - 20)
    playerYRandomVal = random.randint(20, gameWindowHeight - 20)
    while i == False:
        playerXRandomVal = random.randint(0,gameWindowWidth)
        playerYRandomVal = random.randint(0, gameWindowHeight)
        pixelColourPlayer = backGroundIMG.get_at((playerXRandomVal,playerYRandomVal))
        if pixelColourPlayer.r == 255:
            i = True


    position = [playerXRandomVal, playerYRandomVal]
    return position
def collisionChecker(firstGameObject, secondGameObject):
    if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
        return True

screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
backGroundIMG = pygame.surfarray.make_surface(NMF.makeNoiseMap())
upgradeObject = UpgradeClass(screen)

playerObject1 = PlayerClass(backGroundIMG,screen,position=findSpawnForPlayer(),PID=  1)
playerObject2 = PlayerClass(backGroundIMG,screen,position=findSpawnForPlayer(),PID = 2)
players.append(playerObject1)
players.append(playerObject2)
generateEnemy()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True


        #KEY PRESSES:
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            movementfunction(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                backGroundIMG = invertMap()




    #Update functions)
    if players != []:
        for playerObject in players:
            playerObject.update(backGroundIMG)
            if playerObject.playerHP == 0:
                players.remove(playerObject)
        if len(enemies) < upgradeObject.challengeLevel:
            generateEnemy()

        for shot in shots:
            shot.update()
            if shot.x > gameWindowWidth or shot.x < 0 or shot.y > gameWindowHeight or shot.y < 0:
                shots.remove(shot)


        for enemy in enemies:
            enemyDead = False
            enemy.update(backGroundIMG)


            for shot in shots:
                if collisionChecker(shot, enemy):
                    if enemyDead == True:
                        pass
                    else:
                        enemyDead = True

                        shouldGetUpgrade = upgradeObject.update()
                        if shouldGetUpgrade == True:
                            randomUpgrade = random.randint(0,2)
                            for playerObject in players:
                                upgradeObject.upgradePlayers(playerObject,randomUpgrade)


                        shots.remove(shot)
                        enemies.remove(enemy)
            if collisionChecker(enemy, playerObject1):
                playerObject1.playerHP -= 1

            if collisionChecker(enemy, playerObject2):
                playerObject2.playerHP -= 1





        #DRAW GAME OBJECTS:
    #screen.fill((0, 0, 20)) #blank screen. (or maybe draw a background)


    screen.blit(backGroundIMG,(0,0))
    upgradeObject.draw(font)
    if players != []:
        for playerObject in players:
            if playerObject.playerHP < 1:
                upgradeObject.playerDeadTimerVariable = 1
            if upgradeObject.playerDeadTimerVariable < 120 and upgradeObject.playerDeadTimerVariable != 0:
                upgradeObject.playerIsDead(playerObject,screen,font)
        for playerObject in players:
            playerObject.draw()


        for shot in shots:
            shot.draw()

        for enemy in enemies:
            enemy.draw()
    else:
        text_width, text_height = font.size('Everyone is dead')
        text = font.render('Everyone is dead', True, (200, 0, 0))
        screen.blit(text, ((gameWindowWidth - text_width) / 2, (gameWindowHeight - text_height) / 2 - 100))
        text_width, text_height = font.size('Level: '+ str(upgradeObject.challengeLevel))
        text = font.render('Level: '+ str(upgradeObject.challengeLevel), True, (200, 0, 0))
        screen.blit(text, ((gameWindowWidth - text_width) / 2, (gameWindowHeight - text_height) / 2 + 100))
    pygame.display.flip()
    clock.tick(60)




