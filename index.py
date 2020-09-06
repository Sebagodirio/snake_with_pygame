import pygame, sys, time, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake 2.0")
fps = pygame.time.Clock()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((0,0,0))
        pygame.display.flip
        fps.tick(10)
main()
pygame.quit()