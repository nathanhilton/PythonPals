import pygame

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (round(self.x - 2, self.y - 2), round(self.width + 4, self.height + 4)), 0)

        pygame.draw.rect(screen, self.color, (round(self.x), round(self.y), round(self.width), round(self.height)), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (round(self.x + (self.width / 2 - text.get_width() / 2)), round(self.y + (self.height / 2 - text.get_height() / 2))))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

class healthBar():
    def __init__(self, x, y, width, height, health, orientation):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.orientation = orientation

    def set_health(self, newHealth):
        self.health = newHealth

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x - 2, self.y - 2, self.width + 4, self.height + 4))
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        if self.health != 0:
            if self.health >= 55:
                pygame.draw.rect(screen, (0,128,0), (self.x, self.y, self.width - (self.width * ((100-self.health)/100)), self.height))
            elif self.health < 25:
                pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width - (self.width * ((100 - self.health) / 100)), self.height))
            else:
                pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width - (self.width * ((100 - self.health) / 100)), self.height))
            print(self.health)
            # font = pygame.font.SysFont('comicsans', 40)
            # text = font.render("HP:", 1, (0, 0, 0), (204,204,0))
            # text_rect = text.get_rect()
            # text_rect.center = (self.x + (self.width * 0.15), self.y + (self.height * 0.5))
            # screen.blit(text, text_rect)
        pygame.display.update()
