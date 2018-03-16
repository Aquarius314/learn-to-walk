import pygame

SKY_BLUE = (146, 217, 239)


class Gui:

    def display(self, screen):
        pygame.display.flip()
        screen.fill(SKY_BLUE)
