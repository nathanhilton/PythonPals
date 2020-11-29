import os
import pygame
import sys


<<<<<<< Updated upstream
=======
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []

        self.images.append(pygame.image.load('snake1.png'))
        self.images.append(pygame.image.load('Snake_start.png'))
        self.images.append(pygame.image.load('Snake_Firemid.png'))
        self.images.append(pygame.image.load('snake2.png'))
        self.images.append(pygame.image.load('Snake_fire_end.png'))
        self.images.append(pygame.image.load('snake4.png'))
        self.images.append(pygame.image.load('snake6.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(250, 575, 600, 600)

    def resizePlayer(self, scale):
        self.height = self.height * scale
        self.width = self.width * scale
        self.image = pygame.transform.rotozoom(self.images[self.index], 0, scale)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def changeLocation(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Coffee(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('coffee1.png'))
        self.images.append(pygame.image.load('coffee2.png'))
        self.images.append(pygame.image.load('coffee3.png'))
        self.images.append(pygame.image.load('coffee4.png'))
        self.images.append(pygame.image.load('coffee5.png'))
        self.images.append(pygame.image.load('coffee6.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(1000, 450, 500, 500)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def resizeCoffee(self, scale):
        self.height = self.height * scale
        self.width = self.width * scale
        self.image = pygame.transform.rotozoom(self.images[self.index], 0, scale)

    def changeLocation(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Ruby(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('Ruby_idle.png'))
        self.images.append(pygame.image.load('Ruby_left.png'))
        self.images.append(pygame.image.load('Ruby_prep.png'))
        self.images.append(pygame.image.load('Ruby_start.png'))
        self.images.append(pygame.image.load('Ruby_fire.png'))
        self.images.append(pygame.image.load('Ruby_start.png'))
        self.images.append(pygame.image.load('Ruby_prep.png'))
        self.images.append(pygame.image.load('Ruby_left.png'))
        self.images.append(pygame.image.load('Ruby_hurt.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(800, 350, 500, 500)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def resizeRuby(self, scale):
        self.height = self.height * scale
        self.width = self.width * scale
        self.image = pygame.transform.rotozoom(self.images[self.index], 0, scale)

    def changeLocation(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)

class Eye(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('C1.png'))
        self.images.append(pygame.image.load('C2.png'))
        self.images.append(pygame.image.load('C3.png'))
        self.images.append(pygame.image.load('C4.png'))


        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(850, 400, 500, 500)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def resizeEye(self, scale):
        self.height = self.height * scale
        self.width = self.width * scale
        self.image = pygame.transform.rotozoom(self.images[self.index], 0, scale)

    def changeLocation(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)
>>>>>>> Stashed changes
