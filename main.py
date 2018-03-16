import pygame
import time
from algorithm import Algorithm
from gui import Gui
from world import World

print("Starting")

(width, height) = (1500, 500)

screen = pygame.display.set_mode((width, height))
# pygame.display.flip()

pygame.init()

running = True
alg = Algorithm()
gui = Gui()
world = World(width, height)
while running:
    running = alg.calculate(world)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gui.display(screen)
    world.display_world(screen)

pygame.quit()
