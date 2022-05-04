import pygame

class ShotClass:

    width = 5
    height = 5
    color = (255, 165, 0)


    def __init__(self, screen, spawnPosX, spawnPosY, playerSpeedX, playerSpeedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = playerSpeedX
        self.ySpeed = playerSpeedY
        self.theScreen = screen


    def update(self):
        self.x += self.xSpeed
        self.y += self.ySpeed

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))