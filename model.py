import math
import random
import pygame
import time

MODEL_COLOR = (0, 0, 0)
LEG_COLOR = (0, 0, 0)
TIME = 20


def rotate(x, y, radius, angle):
    s = math.sin(angle)
    c = math.cos(angle)
    x += c * radius
    y += s * radius
    return int(x), int(y)


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Model:

    dead = False

    radius = 8
    height = 100

    left_leg_length = 50
    left_leg_angle = 0
    left_leg_point = (0, 0)
    left_leg_stands = False

    right_leg_length = 30
    right_leg_angle = 0
    right_leg_point = (0, 0)
    right_leg_stands = False

    initial_left_angle = 3*math.pi/4
    initial_right_angle = math.pi/4

    def __init__(self, x, y):
        self.start_x = x
        self.head_x = x
        self.head_y = y
        self.leg1_x = x - 20
        self.leg1_y = y + self.height - self.radius
        self.leg2_x = x + 20
        self.leg2_y = y + self.height - self.radius
        self.LEFT_LEG_SPEED = random.randint(-10, 10)/10
        self.LEFT_LEG_STRENGTH = random.randint(-10, 10)/10
        self.RIGHT_LEG_SPEED = random.randint(-10, 10)/10
        self.RIGHT_LEG_STRENGTH = random.randint(-10, 10)/10
        self.LEFT_LEG_FLEXIBILITY = 1 # random.randint(-20, 20)/10
        self.RIGHT_LEG_FLEXIBILITY = 1 # random.randint(-20, 20)/10

    def set_leg_lengths(self, left, right):
        self.left_leg_length = left
        self.right_leg_length = right

    def set_angles(self, left_angle, right_angle):
        self.left_leg_angle = left_angle
        self.right_leg_angle = right_angle

    def display(self, screen):
        if self.dead:
            return
        self.display_leg(self.get_left_leg_point(), screen)
        self.display_leg(self.get_right_leg_point(), screen)
        pygame.draw.circle(screen, MODEL_COLOR, (int(self.head_x), int(self.head_y)), self.radius)
        self.display_distance(screen)

    def display_distance(self, screen):
        pygame.draw.line(screen, (0, 0, 255), (self.start_x, 0), (self.start_x, 1000), 2)
        dist = self.get_distance()
        dist_col = (0, 255, 0)
        if dist < 0:
            dist_col = (255, 0, 0)
            if dist < -200:
                self.dead = True
        # pygame.draw.line(screen, dist_col, (self.start_x, self.head_y), (self.head_x, self.head_y), 2)

    def get_distance(self):
        return self.head_x - self.start_x

    def display_leg(self, leg, screen):
        x, y = leg
        pygame.draw.line(screen, LEG_COLOR, (leg), (int(self.head_x), int(self.head_y)), 3)
        pygame.draw.polygon(screen, MODEL_COLOR, ([(x, y), (x-5, y+self.radius), (x+5, y+self.radius)]))
        # pygame.draw.circle(screen, MODEL_COLOR, (leg), self.radius)

    def move(self, g_line):
        if self.dead:
            return
        lx, ly = self.get_left_leg_point()
        rx, ry = self.get_right_leg_point()
        if ly + self.radius < g_line and ry + self.radius < g_line:
            self.head_y += 0.1
        if ly + self.radius > g_line or ry + self.radius > g_line:
            self.head_y -= 0.1

        self.left_leg_stands = (ly + self.radius == g_line)
        self.right_leg_stands = (ry + self.radius == g_line)

        self.left_leg_angle = \
            self.initial_left_angle + self.LEFT_LEG_STRENGTH*(math.sin(TIME*time.time()*self.LEFT_LEG_SPEED)*self.LEFT_LEG_FLEXIBILITY)/2

        self.right_leg_angle = \
            self.initial_right_angle - self.RIGHT_LEG_STRENGTH*(math.sin(TIME*time.time()*self.RIGHT_LEG_SPEED)*self.RIGHT_LEG_FLEXIBILITY)/2

    def dist_from_head(self, x, y):
        return dist(x, y, self.head_x, self.head_y)

    def get_left_leg_point(self):
        x, y = rotate(self.head_x, self.head_y, self.left_leg_length, self.left_leg_angle)
        if self.left_leg_stands:
            legx, legy = self.left_leg_point
            self.head_x += legx - x
            self.left_leg_point = legx, y
        else:
            self.left_leg_point = x, y
        return self.left_leg_point

    def get_right_leg_point(self):
        x, y = rotate(self.head_x, self.head_y, self.right_leg_length, self.right_leg_angle)
        if self.right_leg_stands:
            legx, legy = self.right_leg_point
            self.head_x += legx - x
            self.right_leg_point = legx, y
        else:
            self.right_leg_point = x, y
        return self.right_leg_point

