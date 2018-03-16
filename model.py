import math
import random
import pygame
import time

MODEL_COLOR = (0, 0, 0)
LEG_COLOR = (0, 0, 0)


def rotate(x, y, radius, angle):
    s = math.sin(angle)
    c = math.cos(angle)
    x += c * radius
    y += s * radius
    return int(x), int(y)


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Model:

    radius = 8
    height = 40
    left_leg_length = 30
    left_leg_angle = 0
    right_leg_length = 30
    right_leg_angle = 0
    initial_left_angle = 3*math.pi/4
    initial_right_angle = math.pi/4
    left_leg_stands = False
    right_leg_stands = False

    def __init__(self, x, y):
        self.head_x = x
        self.head_y = y
        self.leg1_x = x - 20
        self.leg1_y = y + self.height - self.radius
        self.leg2_x = x + 20
        self.leg2_y = y + self.height - self.radius

    def set_angles(self, left_angle, right_angle):
        self.left_leg_angle = left_angle
        self.right_leg_angle = right_angle

    def display(self, screen):
        self.display_leg(self.left_leg_point(), screen)
        self.display_leg(self.right_leg_point(), screen)
        pygame.draw.circle(screen, MODEL_COLOR, (int(self.head_x), int(self.head_y)), self.radius)

    def display_leg(self, leg, screen):
        pygame.draw.line(screen, LEG_COLOR, (leg), (int(self.head_x), int(self.head_y)), 5)
        pygame.draw.circle(screen, MODEL_COLOR, (leg), self.radius)

    def move(self, g_line):
        lx, ly = self.left_leg_point()
        rx, ry = self.right_leg_point()
        if ly + self.radius < g_line and ry + self.radius < g_line:
            self.head_y += 0.1
        if ly + self.radius > g_line or ry + self.radius > g_line:
            self.head_y -= 0.1
        self.left_leg_stands = (ly + self.radius == g_line)
        self.right_leg_stands = (ry + self.radius == g_line)

        self.left_leg_angle = self.initial_left_angle + (math.sin(time.time()*2.5))/2

        self.right_leg_angle = self.initial_right_angle - (math.sin(time.time()))/2

    def dist_from_head(self, x, y):
        return dist(x, y, self.head_x, self.head_y)

    def left_leg_point(self):
        x, y = rotate(self.head_x, self.head_y, self.left_leg_length, self.left_leg_angle)
        if self.left_leg_stands:
            self.head_x -= 0.01
        return x, y

    def right_leg_point(self):
        x, y = rotate(self.head_x, self.head_y, self.right_leg_length, self.right_leg_angle)
        if self.right_leg_stands:
            self.head_x += 0.01
        return x, y

