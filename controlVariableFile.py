import pygame


player1VariableControl = {
    "upVariable": pygame.K_UP,
    "downVariable": pygame.K_DOWN,
    "leftVariable": pygame.K_LEFT,
    "rightVariable": pygame.K_RIGHT,
    "shootVariable": pygame.K_m,
    "teleportVariable": pygame.K_n,
    "color": (255,0,0)
}
player2VariableControl = {
    "upVariable:": pygame.K_w,
    "downVariable": pygame.K_s,
    "leftVariable": pygame.K_a,
    "rightVariable":  pygame.K_d,
    "shootVariable": pygame.K_y,
    "teleportVariable": pygame.K_t,
    "color": (0,0,255),
}


playerVariableList = [player1VariableControl,player2VariableControl]