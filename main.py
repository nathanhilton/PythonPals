import Button
import pygame

pygame.init()

res = (1200, 800)
screen = pygame.display.set_mode(res)
white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
gold = (197, 179, 88)
width = screen.get_width()
height = screen.get_height()
screen.fill(gold)

game_display = pygame.display.set_mode((1200,800))

# all the things needed
startButton = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10), "Start")
optionsButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5), (height * 2 / 10), "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10), "Quit")
userHealth = Button.healthBar(20, 20, 200, 30, 100, "left")
enemyHealth = Button.healthBar(width - 20 - 200, 20, 200, 30, 100, "right")

extraButton = Button.button(color_light, 200, 200, 50, 50, "minus 1")
extraButton2 = Button.button(color_light, 200, 300, 50, 50, "minus 5")
extraButton3 = Button.button(color_light, 200, 400, 50, 50, "minus 10")

def reDrawStartWindow():
    screen.fill(gold)
    font = pygame.font.SysFont('comicsans', 150)
    text = font.render("PythonPals", 1, (0, 0, 0))
    screen.blit(text, (310, 50))
    startButton.draw(screen)
    optionsButton.draw(screen)
    quitButton.draw(screen)

def startscreen():
    reDrawStartWindow()
    while True:
        # reDrawStartWindow()
        pygame.display.update()
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isOver(pos):
                    print("clicked start button")
                    return "start"
                elif optionsButton.isOver(pos):
                    print("clicked options button")
                    return "options"
                elif quitButton.isOver(pos):
                    print("clicked quit button")
                    return "quit"

        pygame.display.update()

def theBattle():
    screen.fill(white)
    coffee = pygame.image.load("coffee1.png")
    snake = pygame.image.load("snake1.png")
    coffee.convert()
    snake.convert()
    coffee = pygame.transform.rotozoom(coffee, 0, 0.5)
    snake = pygame.transform.rotozoom(snake, 0, 0.7)
    health = 100
    extraButton.draw(screen)

    extraButton2.draw(screen)
    extraButton3.draw(screen)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height * 0.1))
    screen.blit(snake, (75, 560))
    screen.blit(coffee, (1000, 550))
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    while True:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if extraButton.isOver(pos):
                    health = health - 1
                    userHealth.set_health(health)
                    userHealth.draw(screen)
                elif extraButton2.isOver(pos):
                    health = health - 5
                    userHealth.set_health(health)
                    userHealth.draw(screen)
                elif extraButton3.isOver(pos):
                    health = health - 10
                    userHealth.set_health(health)
                    userHealth.draw(screen)

# start screen
menuOption = startscreen()

#  go to start, options, or quit
if menuOption == "start":
    theBattle()
elif menuOption == "options":
    print('this is the options')
elif menuOption == "quit":
    pygame.quit()

pygame.quit()
