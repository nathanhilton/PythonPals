import Button
import questions
import pygame
import textwrap

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
    font = pygame.font.SysFont('comicsans', 150)
    text = font.render("PythonPals", 1, (0, 0, 0))
    screen.blit(text, (310, 50))
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

def chooseCategory():
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

def chooseAnswer():
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

def drawBattle():
    screen.fill(white)
    coffee = pygame.image.load("coffee1.png")
    snake = pygame.image.load("snake1.png")
    coffee.convert()
    snake.convert()
    coffee = pygame.transform.rotozoom(coffee, 0, 0.5)
    snake = pygame.transform.rotozoom(snake, 0, 0.7)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height * 0.1))
    screen.blit(snake, (75, 560))
    screen.blit(coffee, (1000, 550))
    enemyHealth.draw(screen)
    userHealth.draw(screen)

def theBattle():
    health = 100
    enemy_health = 100
    userHealth.set_health(health)
    enemyHealth.set_health(enemy_health)

    battle = True
    while battle:
        drawBattle()
        c = chooseCategory()
        questionNumber = questions.load_question(c)
        question, choices, answer = questions.get_question(questionNumber)

        drawBattle()
        q = Button.button(white, 600, 100, 50, 50, textwrap.shorten(question, 100))
        c = Button.button(white, 600, 200, 50, 50, textwrap.shorten(choices, 100))
        q.draw(screen, 30)
        c.draw(screen, 30)

        guess = chooseAnswer()
        is_correct = questions.get_result(guess, answer)

        if is_correct:
            enemy_health = enemy_health - 10
            enemyHealth.set_health(enemy_health)
            enemyHealth.draw(screen)
        else:
            health = health - 10
            userHealth.set_health(health)
            userHealth.draw(screen)

        if health <= 0:
            print("You lost!")
            battle = False
        if enemy_health <= 0:
            print("You won!")
            battle = False
'''
    battle = True
    while battle:
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
            if health <= 0:
                print("You lost!")
                battle = False


def options():
    screen.fill(white)
    menuButton = Button.button(color_light, 200, 200, 50, 50, "Return To Menu")
    print("hi")
    while True:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if mouseButton.isOver(pos):
                    break
    startscreen()
'''


enter_game = True
while enter_game:
    # start screen
    menuOption = startscreen(width, height)

    #  go to start, options, or quit
    if menuOption == "start":
        theBattle()
    elif menuOption == "options":
        print('this is the options')
    elif menuOption == "quit":
        enter_game = False

pygame.quit()