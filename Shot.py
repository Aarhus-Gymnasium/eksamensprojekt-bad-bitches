import pygame

class ShotClass:

    width = 10
    height = 10
    color = (255, 165, 0)


    def __init__(self, screen, spawnPosX, spawnPosY, playerSpeedX, playerSpeedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = playerSpeedX
        self.ySpeed = playerSpeedY
        self.theScreen = screen
        self.deleteTimer = 0


    def update(self):
        self.deleteTimer += 1
        self.x += self.xSpeed * 3
        self.y += self.ySpeed * 3

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))