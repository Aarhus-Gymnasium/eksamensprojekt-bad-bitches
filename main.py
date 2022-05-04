import random
import numpy as np
import NoiseMapFile as NMF
from Player import PlayerClass
from Enemy import EnemyClass
from Shot import ShotClass
from upgradeFile import UpgradeClass
import pygame


pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)


clock = pygame.time.Clock()
gameWindowHeight=1024
gameWindowWidth=1024
enemies=[]
shots = []

def generateEnemy():
    whoToTarget = random.randint(0,1)
    if whoToTarget == 0:
        enemy = EnemyClass(screen= screen,player= playerObject1,BG =backGroundIMG)
    else:
        enemy = EnemyClass(screen= screen,player= playerObject2,BG = backGroundIMG)

    pixelColour = backGroundIMG.get_at((enemy.x, enemy.y))
    if pixelColour.r == 0:
        generateEnemy()
    else:
        enemies.append(enemy)

def findSpawnForPlayer():
    i = False
    playerXRandomVal = random.randint(0, gameWindowWidth)
    playerYRandomVal = random.randint(0, gameWindowHeight)
    while i == False:
        playerXRandomVal = random.randint(0,gameWindowWidth)
        playerYRandomVal = random.randint(0, gameWindowHeight)
        pixelColourPlayer = backGroundIMG.get_at((playerXRandomVal,playerYRandomVal))
        if pixelColourPlayer.r == 255:
            i = True


    position = [playerXRandomVal, playerYRandomVal]
    return position



def invertMap():
    temp = pygame.surfarray.array2d(backGroundIMG)
    blank = np.full((gameWindowWidth, gameWindowHeight), 255)
    inverted = blank - temp
    surface = pygame.surfarray.make_surface(inverted)
    return surface

screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
backGroundIMG = pygame.surfarray.make_surface(NMF.makeNoiseMap())
upgradeObject = UpgradeClass(screen)

def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True


playerObject1 = PlayerClass(backGroundIMG,screen,position=findSpawnForPlayer(),PID=  1)


playerObject2 = PlayerClass(backGroundIMG,screen,position=findSpawnForPlayer(),PID = 2)

for i in range(5):
    generateEnemy()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True


        #KEY PRESSES:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerObject1.ySpeed -= playerObject1.maxSpeed
            if event.key == pygame.K_DOWN:
                playerObject1.ySpeed += playerObject1.maxSpeed
            if event.key == pygame.K_LEFT:
                playerObject1.xSpeed -= playerObject1.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject1.xSpeed += playerObject1.maxSpeed
            if event.key == pygame.K_SPACE:
                backGroundIMG = invertMap()
            if event.key == pygame.K_m:
                shots.append(ShotClass(screen, spawnPosX=playerObject1.x + playerObject1.width / 2, spawnPosY=playerObject1.y + playerObject1.height / 2, playerSpeedX=playerObject1.xSpeed, playerSpeedY=playerObject1.ySpeed))
                if playerObject1.doubleShotPower == True:
                    shots.append(ShotClass(screen, spawnPosX=playerObject1.x + playerObject1.width / 2, spawnPosY=playerObject1.y + playerObject1.height / 2, playerSpeedX=playerObject1.xSpeed - (playerObject1.ySpeed / 2), playerSpeedY=playerObject1.ySpeed + (playerObject1.xSpeed / 2)))
                    shots.append(ShotClass(screen, spawnPosX=playerObject1.x + playerObject1.width / 2, spawnPosY=playerObject1.y + playerObject1.height / 2, playerSpeedX=playerObject1.xSpeed + (playerObject1.ySpeed / 2), playerSpeedY=playerObject1.ySpeed - (playerObject1.xSpeed / 2)))




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerObject1.ySpeed += playerObject1.maxSpeed
            if event.key == pygame.K_DOWN:
                playerObject1.ySpeed -= playerObject1.maxSpeed
            if event.key == pygame.K_LEFT:
                playerObject1.xSpeed += playerObject1.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject1.xSpeed -= playerObject1.maxSpeed

        # KEY PRESSES:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                playerObject2.ySpeed -= playerObject2.maxSpeed
            if event.key == pygame.K_s:
                playerObject2.ySpeed += playerObject2.maxSpeed
            if event.key == pygame.K_a:
                playerObject2.xSpeed -= playerObject2.maxSpeed
            if event.key == pygame.K_d:
                playerObject2.xSpeed += playerObject2.maxSpeed
            if event.key == pygame.K_t:
                shots.append(ShotClass(screen, spawnPosX=playerObject2.x + playerObject2.width / 2, spawnPosY=playerObject2.y + playerObject2.height / 2, playerSpeedX=playerObject2.xSpeed, playerSpeedY=playerObject2.ySpeed))
                if playerObject2.doubleShotPower == True:
                    shots.append(ShotClass(screen, spawnPosX=playerObject2.x + playerObject2.width / 2, spawnPosY=playerObject2.y + playerObject2.height / 2, playerSpeedX=playerObject2.xSpeed - (playerObject2.ySpeed / 2), playerSpeedY=playerObject2.ySpeed + (playerObject2.xSpeed / 2)))
                    shots.append(ShotClass(screen, spawnPosX=playerObject2.x + playerObject2.width / 2, spawnPosY=playerObject2.y + playerObject2.height / 2, playerSpeedX=playerObject2.xSpeed + (playerObject2.ySpeed / 2), playerSpeedY=playerObject2.ySpeed - (playerObject2.xSpeed / 2)))




        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerObject2.ySpeed += playerObject2.maxSpeed
            if event.key == pygame.K_s:
                playerObject2.ySpeed -= playerObject2.maxSpeed
            if event.key == pygame.K_a:
                playerObject2.xSpeed += playerObject2.maxSpeed
            if event.key == pygame.K_d:
                playerObject2.xSpeed -= playerObject2.maxSpeed

    playerObject1.update(backGroundIMG)
    playerObject2.update(backGroundIMG)
    if len(enemies) < 5:
        generateEnemy()

    for shot in shots:
        shot.update()

    for enemy in enemies:
        enemyDead = False
        enemy.update(backGroundIMG)


        #if enemy.x > gameWindowWidth or enemy.y > gameWindowHeight or enemy.x < 0 or enemy.y < 0:
            #enemyDead = True

        for shot in shots:
            if collisionChecker(shot, enemy):
                enemyDead = True
                upgradeObject.update(playerObject1, playerObject2)
                shots.remove(shot)
                enemies.remove(enemy)
        if collisionChecker(enemy, playerObject1):
            playerObject1.playerHP -= 1
            print("OUCH!")
        if collisionChecker(enemy, playerObject2):
            playerObject2.playerHP -= 1
            print("OUCH!!!!")



        #DRAW GAME OBJECTS:
    #screen.fill((0, 0, 20)) #blank screen. (or maybe draw a background)
    screen.blit(backGroundIMG,(0,0))
    upgradeObject.draw()

    playerObject1.draw()
    playerObject2.draw()

    for shot in shots:
        shot.draw()

    for enemy in enemies:
        enemy.draw()
    pygame.display.flip()
    clock.tick(60)




