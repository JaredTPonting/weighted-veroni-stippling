import pygame

pygame.init()

surface = pygame.display.set_mode((400,300))

colour = (255,0,0)

pygame.draw.rect(surface, colour, pygame.Rect(30, 30, 60, 60))
pygame.display.flip()


