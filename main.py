import Button
import questions
import pygame
import textwrap
from player import Player, Coffee

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
white = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
fuschia = (255, 0, 255)
transparent = (0, 0, 0)
gold = (197, 179, 88)
width = screen.get_width()
height = screen.get_height()
screen.fill(gold)


# all the things needed
startButton = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10), "Start")
optionsButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5), (height * 2 / 10), "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10), "Quit")
userHealth = Button.healthBar(20, 20, 200, 30, 100, "left")
enemyHealth = Button.healthBar(width - 20 - 200, 20, 200, 30, 100, "right")
title = Button.text(gold, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150, "PythonPals")
'''
extraButton = Button.button(color_light, 200, 200, 50, 50, "minus 1")
extraButton2 = Button.button(color_light, 200, 300, 50, 50, "minus 5")
extraButton3 = Button.button(color_light, 200, 400, 50, 50, "minus 10")
'''
cat1 = Button.button(fuschia, 200, 100, 50, 50, "cat 1")
cat2 = Button.button(fuschia, 200, 200, 50, 50, "cat 2")
cat3 = Button.button(fuschia, 200, 300, 50, 50, "cat 3")
cat4 = Button.button(fuschia, 200, 400, 50, 50, "cat 4")
cat5 = Button.button(fuschia, 200, 500, 50, 50, "cat 5")

a = Button.button(color_light, 200, 100, 50, 50, "a")
b = Button.button(color_light, 200, 200, 50, 50, "b")
c = Button.button(color_light, 200, 300, 50, 50, "c")
d = Button.button(color_light, 200, 400, 50, 50, "d")

def reDrawStartWindow(width, height):
    screen.fill(gold)
    title.draw(screen)
    startButton.draw(screen, 60)
    optionsButton.draw(screen, 60)
    quitButton.draw(screen, 60)

def startscreen(width, height):
    reDrawStartWindow(width, height)
    while True:
        # reDrawStartWindow()
        pygame.display.update()
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.VIDEORESIZE:
                startWidth = ev.w
                startHeight = ev.h
                startButton.modify((startWidth * 0.25), (startHeight * 3 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
                optionsButton.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
                quitButton.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
                title.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
                width = startWidth
                height = startHeight
                reDrawStartWindow(startWidth, startHeight)
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

def chooseCategory(playerGroup, enemyGroup):
    cat1.draw(screen, 60)
    cat2.draw(screen, 60)
    cat3.draw(screen, 60)
    cat4.draw(screen, 60)
    cat5.draw(screen, 60)
    while True:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if cat1.isOver(pos):
                    return 1
                elif cat2.isOver(pos):
                    return 2
                elif cat3.isOver(pos):
                    return 3
                elif cat4.isOver(pos):
                    return 4
                elif cat5.isOver(pos):
                    return 5

            if ev.type == pygame.VIDEORESIZE:
                print("you are in it")
                startWidth = ev.w
                startHeight = ev.h
                userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                drawBattle(playerGroup, enemyGroup, startWidth, startHeight)
                #pygame.draw.rect(screen, (0, 0, 0), (0, 0, startWidth, startHeight * 0.07))
                #enemyHealth.draw(screen)
                #userHealth.draw(screen)

def chooseAnswer(playerGroup, enemyGroup):
    a.draw(screen, 60)
    b.draw(screen, 60)
    c.draw(screen, 60)
    d.draw(screen, 60)
    while True:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if a.isOver(pos):
                    return 'a'
                elif b.isOver(pos):
                    return 'b'
                elif c.isOver(pos):
                    return 'c'
                elif d.isOver(pos):
                    return 'd'
            if ev.type == pygame.VIDEORESIZE:
                print("you are in it")
                startWidth = ev.w
                startHeight = ev.h
                userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                drawBattle(playerGroup, enemyGroup, startWidth, startHeight)
                #pygame.draw.rect(screen, (0, 0, 0), (0, 0, startWidth, startHeight * 0.07))
                #enemyHealth.draw(screen)
                #userHealth.draw(screen)

def drawBattle(playerGroup, enemyGroup, width, height):
    pygame.display.update()
    screen.fill(white)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height * 0.07))
    playerGroup.draw(screen)
    enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    pygame.display.update()

def theBattle():
    health = 100
    enemy_health = 100
    userHealth.set_health(health)
    enemyHealth.set_health(enemy_health)

    clock = pygame.time.Clock()

    myPlayer = Player()
    playerGroup = pygame.sprite.Group(myPlayer)
    playerGroup.draw(screen)

    myEnemy = Coffee()
    enemyGroup = pygame.sprite.Group(myEnemy)
    enemyGroup.draw(screen)
    pygame.display.update()



    battle = True
    while battle:
        clock.tick(27)

        drawBattle(playerGroup, enemyGroup, screen.get_width(), screen.get_height())
        c = chooseCategory(playerGroup, enemyGroup)
        questionNumber = questions.load_question(c)
        question, choices, answer = questions.get_question(questionNumber)

        drawBattle(playerGroup, enemyGroup, screen.get_width(), screen.get_height())
        q = Button.button(white, 600, 100, 50, 50, textwrap.shorten(question, 100))
        c = Button.button(white, 600, 200, 50, 50, textwrap.shorten(choices, 100))
        q.draw(screen, 30)
        c.draw(screen, 30)

        guess = chooseAnswer(playerGroup, enemyGroup)
        is_correct = questions.get_result(guess, answer)

        if is_correct:
            enemy_health = enemy_health - 25
            enemyHealth.set_health(enemy_health)
            enemyHealth.draw(screen)

            clock.tick(2)
            pygame.draw.rect(screen, white, (200, 500, 500, 500))
            playerGroup.update()
            playerGroup.draw(screen)
            pygame.display.update()
            clock.tick(2)
            pygame.draw.rect(screen, white, (200, 500, 500, 500))
            playerGroup.update()
            playerGroup.update()
            playerGroup.draw(screen)
            pygame.display.update()

            pygame.draw.rect(screen, white, (700, 400, 500, 500))
            enemyGroup.update()
            enemyGroup.update()
            enemyGroup.update()
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            pygame.draw.rect(screen, white, (700, 400, 500, 500))
            enemyGroup.update()
            enemyGroup.draw(screen)
            pygame.display.update()


        else:
            health = health - 10
            userHealth.set_health(health)
            userHealth.draw(screen)

            clock.tick(3)
            pygame.draw.rect(screen, white, (700, 400, 500, 500))
            enemyGroup.update()
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            pygame.draw.rect(screen, white, (700, 400, 500, 500))
            enemyGroup.update()
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            pygame.draw.rect(screen, white, (700, 400, 500, 500))
            enemyGroup.update()
            enemyGroup.update()
            enemyGroup.draw(screen)
            pygame.display.update()


            pygame.draw.rect(screen, white, (200, 500, 500, 500))
            playerGroup.update()
            playerGroup.update()
            playerGroup.draw(screen)
            pygame.display.update()
            clock.tick(2)
            pygame.draw.rect(screen, white, (200, 500, 500, 500))
            playerGroup.update()
            playerGroup.draw(screen)
            pygame.display.update()

        if health <= 0:
            print("You lost!")
            battle = False
            screen.fill((100,100,100))
            snake = pygame.image.load("snake5.png")
            snake.convert()
            snake = pygame.transform.rotozoom(snake, 0, 0.7)
            screen.blit(snake, (75, 560))
            gameOver = Button.text(gold, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                                "GameOver")
            gameOver.draw(screen)
            clock.tick(2)
            pygame.display.update()
            pygame.time.delay(4000)

        if enemy_health <= 0:
            print("You won!")
            battle = False
            screen.fill((100,100,100))
            snake = pygame.image.load("snake6.png")
            snake.convert()
            snake = pygame.transform.rotozoom(snake, 0, 0.7)
            screen.blit(snake, (75, 560))
            winScreen = Button.text(gold, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                                    "You win!")
            winScreen.draw(screen)
            clock.tick(2)
            pygame.display.update()
            pygame.time.delay(4000)



enter_game = True
while enter_game:
    # start screen
    menuOption = startscreen(width, height)

    #  go to start, options, or quit
    if menuOption == "start":
        result = theBattle()
    elif menuOption == "options":
        print('this is the options')
    elif menuOption == "quit":
        enter_game = False

pygame.quit()