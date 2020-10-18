import os
import pygame
import sys


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # super(Player, self).__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('snake1.png'))
        self.images.append(pygame.image.load('snake2.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(200, 500, 500, 500)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

class Coffee(pygame.sprite.Sprite):

    def __init__(self):
        # super(Player, self).__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('coffee1.png'))
        self.images.append(pygame.image.load('coffee2.png'))
        self.images.append(pygame.image.load('coffee3.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(700, 400, 500, 500)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]