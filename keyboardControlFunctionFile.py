import pygame
from Shot import ShotClass


def movementfunction(playerObject,event,shots,screen):
    if event.type == pygame.KEYDOWN:
        if event.key == playerObject.upVariable:
            playerObject.ySpeed -= playerObject.maxSpeed
        if event.key == playerObject.downVariable:
            playerObject.ySpeed += playerObject.maxSpeed
        if event.key == playerObject.leftVariable:
            playerObject.xSpeed -= playerObject.maxSpeed
        if event.key == playerObject.rightVariable:
            playerObject.xSpeed += playerObject.maxSpeed



        if event.key == playerObject.shootVariable:
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
        if event.key == playerObject.teleportVariable:
            playerObject.teleportBack()

    if event.type == pygame.KEYUP:
        if event.key == playerObject.upVariable:
            playerObject.ySpeed += playerObject.maxSpeed
        if event.key ==playerObject.downVariable:
            playerObject.ySpeed -= playerObject.maxSpeed
        if event.key == playerObject.leftVariable:
            playerObject.xSpeed += playerObject.maxSpeed
        if event.key == playerObject.rightVariable:
            playerObject.xSpeed -= playerObject.maxSpeed