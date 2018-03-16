import pygame
import time
from algorithm import Algorithm
from gui import Gui
from world import World

print("Starting")

(width, height) = (500, 500)

screen = pygame.display.set_mode((width, height))
# pygame.display.flip()

pygame.init()

running = True
alg = Algorithm()
gui = Gui()
world = World(width, height)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    alg.calculate(world)
    gui.display(screen)
    world.display_world(screen)

pygame.quit()
