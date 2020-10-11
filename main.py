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

# all the things needed
startButton = Button.button(color_light, (width * 0.25), (height * 1 / 10), (width * 0.5), (height * 2 / 10), "Start")
optionsButton = Button.button(color_light, (width * 0.25), (height * 4 / 10), (width * 0.5), (height * 2 / 10), "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 7 / 10), (width * 0.5), (height * 2 / 10), "Quit")

userHealth = Button.healthBar(20, 20, 150, 40, 100, "left");

def reDrawStartWindow():
    screen.fill(gold)
    startButton.draw(screen)
    optionsButton.draw(screen)
    quitButton.draw(screen)

def startscreen():
    while True:
        reDrawStartWindow()
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
    while True:
        userHealth.draw(screen)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()

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
