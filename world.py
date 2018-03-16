import pygame
import time
from model import Model
import random

POPULATION_SIZE = 50


class World:

    ground_line = 300
    models = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        for i in range(POPULATION_SIZE):
            model = Model(300, self.ground_line - 100)
            model.set_leg_lengths(random.randint(0, 50)+10, random.randint(0, 50)+10)
            self.models.append(model)

    def display_world(self, screen):
        brown = (112, 76, 22)
        pygame.draw.rect(screen, brown, (0, self.ground_line, self.width, self.height))
        for model in self.models:
            model.display(screen)
