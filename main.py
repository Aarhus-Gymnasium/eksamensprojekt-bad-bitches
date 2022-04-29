import random

import NoiseMapFile as NMF
from Player import PlayerClass
from Enemy import EnemyClass
import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)


clock = pygame.time.Clock()
gameWindowHeight=1024
gameWindowWidth=1024
enemies=[]

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

def generateMap():
    global backGroundIMG
    backGroundIMG = pygame.surfarray.make_surface(NMF.makeNoiseMap())
    pixelColourPlayer1 = backGroundIMG.get_at((590, 100))
    pixelColourPlayer2 = backGroundIMG.get_at((890, 100))
    if pixelColourPlayer1.r == 0:
        generateMap()
    elif pixelColourPlayer2.r == 0:
        generateMap()
    else:
        return backGroundIMG
screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))
backGroundIMG = pygame.surfarray.make_surface(NMF.makeNoiseMap())
generateMap()

def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True

playerObject1 = PlayerClass(backGroundIMG,screen,xpos=590, ypos=100)

playerObject2 = PlayerClass(backGroundIMG,screen,xpos=890, ypos=100)

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                playerObject2.ySpeed += playerObject2.maxSpeed
            if event.key == pygame.K_s:
                playerObject2.ySpeed -= playerObject2.maxSpeed
            if event.key == pygame.K_a:
                playerObject2.xSpeed += playerObject2.maxSpeed
            if event.key == pygame.K_d:
                playerObject2.xSpeed -= playerObject2.maxSpeed

    playerObject1.update()
    playerObject2.update()

    for enemy in enemies:
        enemy.update()

        #DRAW GAME OBJECTS:
    #screen.fill((0, 0, 20)) #blank screen. (or maybe draw a background)
    screen.blit(backGroundIMG,(0,0))

    playerObject1.draw()
    playerObject2.draw()

    for enemy in enemies:
        enemy.draw()
    pygame.display.flip()
    clock.tick(60)




