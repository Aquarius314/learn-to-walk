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
        # model1 = Model(200, self.ground_line - 220)
        # model1.set_leg_lengths(50, 50)
        # self.models.append(model1)
        # model2 = Model(300, self.ground_line - 220)
        # model2.set_leg_lengths(50, 50)
        # self.models.append(model2)
        # model3 = Model(400, self.ground_line - 220)
        # model3.set_leg_lengths(50, 50)
        # self.models.append(model3)
        for i in range(POPULATION_SIZE):
            model = Model(300, self.ground_line - 100)
            model.set_leg_lengths(random.randint(0, 40)+30, random.randint(0, 40)+30)
            self.models.append(model)

    def display_world(self, screen):
        brown = (112, 76, 22)
        pygame.draw.rect(screen, brown, (0, self.ground_line, self.width, self.height))
        for model in self.models:
            model.display(screen)
