import sys
import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))

font = pygame.font.SysFont("Times New Roman", 50)
font2 = pygame.font.SysFont("Courier New", 50)

score = 0

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    #print("asdf")
    score += 1

    text1 = font2.render("Text! " + str(score), True, "red")
    text2 = font.render(f"Text! {score}", False, "red")

    screen.fill("black")
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 100))

    pygame.display.flip()

'''
For text in pygame!
1. initialize the font: font = pygame.font.SysFont("Times New Roman", 50)

2. define a font variable to render: font.render(f"Text! {score}", False, "red")

3. draw the font on the screen in a position: screen.blit(text2, (10, 100))
'''