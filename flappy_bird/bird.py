import pygame
import math
radius = 10
width = 700
height = 500

class Bird(pygame.sprite.Sprite):
    def __init__(self, win, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.win = win
        self.gravity = 1
        self.ySpeed = 2
        self.image = pygame.image.load("bird.jpg")
        self.image = pygame.transform.scale(self.image, (radius, radius))
        self.rect = self.image.get_rect()

    def show(self):
        pygame.draw.circle(self.win, (252, 255, 255), (self.x, self.y), radius)

    def update(self):
        self.y += math.floor(self.ySpeed)
        self.ySpeed += self.gravity
        self.ySpeed *= 0.9999
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     self.jump()

    def jump(self):
        self.ySpeed = -10 * self.gravity

    def die(self, obs):
        if self.y >= height or self.y <= 0:
            return True

        if self.x + 10 >= obs.x:
            if self.y + 10 <= obs.height or self.y + 10 >= obs.height + obs.gap:
                return True
        return False
