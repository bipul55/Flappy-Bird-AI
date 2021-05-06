import random
import pygame

width = 700
height = 500


class Obstacle:
    def __init__(self, win, x):
        self.gap = random.randint(100, 150)
        self.height = random.randint(50, height - self.gap - 50)
        # print(self.gap , self.height)
        self.x = x
        self.width = 40
        self.win = win
        self.vel = 5

    def show(self):
        pygame.draw.rect(self.win, (255, 255, 255), (self.x, 0, self.width, self.height))
        pygame.draw.rect(self.win, (255, 255, 255),
                         (self.x, self.height + self.gap, self.width, width - self.height + self.gap))

    def update(self):
        self.x -= self.vel
