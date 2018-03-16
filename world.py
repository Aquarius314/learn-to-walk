import pygame
import time
from model import Model


class World:

    ground_line = 300
    models = []

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.models.append(Model(300, self.ground_line - 240))
        model2 = Model(200, self.ground_line - 220)
        self.models.append(model2)

    def display_world(self, screen):
        brown = (112, 76, 22)
        pygame.draw.rect(screen, brown, (0, self.ground_line, self.width, self.height))
        for model in self.models:
            model.display(screen)
