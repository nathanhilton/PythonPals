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


def reDrawWinodw():
    screen.fill(gold)
    startButton.draw(screen)
    optionsButton.draw(screen)
    quitButton.draw(screen)


startButton = Button.button(color_light, (width * 0.25),  (height * 1 / 10), (width * 0.5), (height * 2 / 10), "Start")
optionsButton = Button.button(color_light,(width * 0.25), (height * 4 / 10), (width * 0.5), (height * 2 / 10), "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 7 / 10), (width * 0.5), (height * 2 / 10), "Quit")
run = True

while run:
    reDrawWinodw()
    pygame.display.update()
    for ev in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if ev.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if startButton.isOver(pos):
                print("clicked the start button")
            elif optionsButton.isOver(pos):
                print("clicked options button")
            elif quitButton.isOver(pos):
                print("clicked quit button")

    pygame.display.update()

pygame.quit()