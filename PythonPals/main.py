import Button
import questions
import pygame
import pygame.gfxdraw
import textwrap
from player import Player, Coffee


class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height

screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
white = (255, 255, 255)
purple = (110, 113, 198)
indigo = (51, 57, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
fuschia = (255, 0, 255)
black = (0, 0, 0)
gold = (197, 179, 88)
lime = (153, 255, 51)
width = screen.get_width()
height = screen.get_height()
screen.fill(gold)

clock = pygame.time.Clock()

theScreen = Screen(screen.get_width(), screen.get_height())

# all the things needed
startButton = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10),
                                       "Start")
optionsButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5),
                                         (height * 2 / 10), "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Quit")


userHealth = Button.healthBar(20, 20, 200, 30, 100, "left")
enemyHealth = Button.healthBar(width - 20 - 200, 20, 200, 30, 100, "right")
title = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               "PYTHON PALS")
# level = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.4, theScreen.width * 0.5, theScreen.height * 0.2, "LEVEL 1")
'''
extraButton =Button.button(color_light, 200, 200, 50, 50, "minus 1")
extraButton2 =Button.button(color_light, 200, 300, 50, 50, "minus 5")
extraButton3 =Button.button(color_light, 200, 400, 50, 50, "minus 10")
'''
cat1 = Button.button(fuschia, 200, 200, 30, 30, " Syntax")
cat2 = Button.button(fuschia, 450, 200, 30, 30, " Vocabulary")
cat3 = Button.button(fuschia, 700, 200, 30, 30, " Logic")
cat4 = Button.button(fuschia, 150, 350, 30, 30, " Number Conversion")
cat5 = Button.button(fuschia, 550, 350, 30, 30, " General")

a = Button.button(color_light, 200, 175, 25, 25)
b = Button.button(color_light, 200, 225, 25, 25)
c = Button.button(color_light, 200, 275, 25, 25)
d = Button.button(color_light, 200, 325, 25, 25)

chooseCat = Button.text(fuschia, (theScreen.width * 0.25), (theScreen.height * 0 / 12), (theScreen.width * 0.5),
                            (theScreen.height * 1 / 10),
                            100, "Choose a category:")

back_to_main = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Back to Main Menu")

option = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               "OPTIONS")

changeButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5), (height * 2 / 10),
                                      "Change Deck")


def resize(startWidth, startHeight):
    startButton.modify((startWidth * 0.25), (startHeight * 3 / 12), (startWidth * 0.5),
                       (startHeight * 2 / 10))
    optionsButton.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5),
                         (startHeight * 2 / 10))
    quitButton.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                      (startHeight * 2 / 10))
    title.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    changeButton.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))
    back_to_main.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))
    option.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    theScreen.width = startWidth
    theScreen.height = startHeight

def reDrawStartWindow():
    screen.fill(gold)
    title.draw(screen, int(theScreen.width*0.1), True)
    startButton.draw(screen, int(theScreen.width*0.05), True)
    optionsButton.draw(screen, int(theScreen.width*0.05), True)
    quitButton.draw(screen, int(theScreen.width*0.05), True)

def startscreen(width, height):
    reDrawStartWindow()
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
                resize(startWidth, startHeight)
                reDrawStartWindow()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if startButton.isOver(pos):
                    # print("clicked start button")
                    return "start"
                elif optionsButton.isOver(pos):
                    # print("clicked options button")
                    return "options"
                elif quitButton.isOver(pos):
                    # print("clicked quit button")
                    return "quit"

        pygame.display.update()

def drawCategories():
    chooseCat.draw(screen, int(theScreen.width * 0.07), True)
    cat1.draw(screen, int(theScreen.width * 0.02))
    cat2.draw(screen, int(theScreen.width * 0.02))
    cat3.draw(screen, int(theScreen.width * 0.02))
    cat4.draw(screen, int(theScreen.width * 0.02))
    cat5.draw(screen, int(theScreen.width * 0.02))

def chooseCategory(playerGroup, enemyGroup):
    drawCategories()
    while True:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if cat1.isOver(pos):
                    print(1)
                    return 1
                elif cat2.isOver(pos):
                    print(2)
                    return 2
                elif cat3.isOver(pos):
                    print(3)
                    return 3
                elif cat4.isOver(pos):
                    print(4)
                    return 4
                elif cat5.isOver(pos):
                    print(5)
                    return 5

            if ev.type == pygame.VIDEORESIZE:
                # print("you are in it")
                startWidth = ev.w
                startHeight = ev.h
                theScreen.width = startWidth
                theScreen.height = startHeight
                userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                drawBattle(playerGroup, enemyGroup, startWidth, startHeight)
                chooseCategory(playerGroup, enemyGroup)
                #resizeBattle()
                #drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height)
                #chooseCategory(playerGroup, enemyGroup)
                #drawCategories()
                # pygame.draw.rect(screen, (0, 0, 0), (0, 0, startWidth, startHeight * 0.07))
                # enemyHealth.draw(screen)
                # userHealth.draw(screen)

def resizeBattle():
    startWidth = theScreen.width
    startHeight = theScreen.height
    userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    '''
    a.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    b.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    c.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    d.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    chooseCat.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    cat1.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    cat2.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    cat3.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    cat4.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    cat5.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
'''

def drawAnswers():
    a.draw(screen, int(theScreen.width * 0.02))
    b.draw(screen, int(theScreen.width * 0.02))
    c.draw(screen, int(theScreen.width * 0.02))
    d.draw(screen, int(theScreen.width * 0.02))

def chooseAnswer(playerGroup, enemyGroup, question):
    drawAnswers()
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
                #resizeBattle()
                #drawAnswers()
                startWidth = ev.w
                startHeight = ev.h
                theScreen.width = startWidth
                theScreen.height = startHeight
                userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
                drawBattle(playerGroup, enemyGroup, startWidth, startHeight)
                # pygame.draw.rect(screen, (0, 0, 0), (0, 0, startWidth, startHeight * 0.07))
                # enemyHealth.draw(screen)
                # userHealth.draw(screen)


def drawBattle(playerGroup, enemyGroup, width, height):
    pygame.display.update()
    # screen.fill(white)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.1))
    bg = pygame.image.load("jungleBackground.jpg")
    bg = pygame.transform.rotozoom(bg, 0, theScreen.width/ 1380)
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.07))
    playerGroup.draw(screen)
    enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    pygame.display.update()


def drawBackground(playerGroup, enemyGroup, width, height):
    pygame.display.update()
    # screen.fill(white)

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.07))
    bg = pygame.image.load("jungleBackground.jpg")
    bg = pygame.transform.rotozoom(bg, 0, theScreen.width / 1380)
    screen.blit(bg,(0,0))
    # playerGroup.draw(screen)
    # enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    pygame.display.update()

# def playAnimation(groupA,groupB,numFramesA,numFramesB,screen,width,height,clock,clockSpeed):
#     for i in range(0,numFramesA):
#         groupA.update()
#


def theBattle():
    health = 100
    enemy_health = 100
    userHealth.set_health(health)
    enemyHealth.set_health(enemy_health)

    clock = pygame.time.Clock()

    # background music
    pygame.mixer.music.load('jazz.mp3')
    pygame.mixer.music.play(-1)

    myPlayer = Player()
    playerGroup = pygame.sprite.Group(myPlayer)
    # playerGroup.draw(screen)

    myEnemy = Coffee()
    enemyGroup = pygame.sprite.Group(myEnemy)
    # enemyGroup.draw(screen)
    pygame.display.update()

    battle = True
    while battle:
        clock.tick(27)
        userHealth.modify(0.02 * theScreen.width, 0.02 * theScreen.height, theScreen.width * 0.1,
                          theScreen.height * 0.03)
        enemyHealth.modify(0.88 * theScreen.width, 0.02 * theScreen.height, theScreen.width * 0.1,
                           theScreen.height * 0.03)
        # enemyGroup.draw(screen)
        # playerGroup.draw(screen)
        drawBattle(playerGroup, enemyGroup, width, height)
        choose = chooseCategory(playerGroup, enemyGroup)
        print(choose)
        questionNumber = questions.load_question(choose)
        question = questions.get_question(questionNumber)

        drawBattle(playerGroup, enemyGroup, width, height)
        q = Button.text(black, 600, 100, 50, 50, 40, textwrap.shorten(question[0], 100))
        pygame.gfxdraw.box(screen, pygame.Rect(0, theScreen.height * 0.1, theScreen.width, 75),
                           (77, 153, 83, 130))
        A = Button.text(black, a.x, a.y, 50, 50, 40, textwrap.shorten(question[1], 100))
        B = Button.text(black, b.x, b.y, 50, 50, 40, textwrap.shorten(question[2], 100))
        C = Button.text(black, c.x, c.y, 50, 50, 40, textwrap.shorten(question[3], 100))
        D = Button.text(black, d.x, d.y, 50, 50, 40, textwrap.shorten(question[4], 100))
        pygame.gfxdraw.box(screen, pygame.Rect(theScreen.width * 0.1, theScreen.height * 0.15,
                                               600, 300), (77, 153, 83, 130))
        q.draw(screen, int(theScreen.width*0.02), True)
        A.draw(screen, int(theScreen.width*0.015), False)
        B.draw(screen, int(theScreen.width*0.015), False)
        C.draw(screen, int(theScreen.width*0.015), False)
        D.draw(screen, int(theScreen.width*0.015), False)

        guess = chooseAnswer(playerGroup, enemyGroup, question)
        is_correct = questions.get_result(guess, question[5])

        if is_correct:
            enemy_health = enemy_health - 25
            enemyHealth.set_health(enemy_health)
            enemyHealth.draw(screen)

            clock.tick(4)

            for i in range(0, 4):
                drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
                playerGroup.update()
                playerGroup.draw(screen)
                enemyGroup.draw(screen)
                pygame.display.update()
                clock.tick(4)

            # pygame.draw.rect(screen, white, (200, 500, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            playerGroup.update()
            playerGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()

            # pygame.draw.rect(screen, white, (700, 400, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            enemyGroup.update()
            enemyGroup.update()
            enemyGroup.update()
            enemyGroup.draw(screen)
            playerGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            # pygame.draw.rect(screen, white, (700, 400, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            enemyGroup.update()
            enemyGroup.draw(screen)
            playerGroup.draw(screen)
            pygame.display.update()


        else:
            health = health - 10
            userHealth.set_health(health)
            userHealth.draw(screen)

            clock.tick(3)
            # pygame.draw.rect(screen, white, (700, 400, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            enemyGroup.update()
            enemyGroup.draw(screen)
            playerGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            # pygame.draw.rect(screen, white, (700, 400, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            enemyGroup.update()
            enemyGroup.draw(screen)
            playerGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            # pygame.draw.rect(screen, white, (700, 400, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            enemyGroup.update()
            enemyGroup.update()
            enemyGroup.draw(screen)
            playerGroup.draw(screen)
            pygame.display.update()

            # pygame.draw.rect(screen, white, (200, 500, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            for i in range(0, 4):
                playerGroup.update()
            playerGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(3)
            # pygame.draw.rect(screen, white, (200, 500, 500, 500))
            drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
            playerGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()

        if health <= 0:
            battle = False
            return "lose"

        if enemy_health <= 0:
            battle = False
            return "win"

def win():
    print("You won!")
    screen.fill((100, 100, 100))
    snake = pygame.image.load("snake6.png")
    snake.convert()
    snake = pygame.transform.rotozoom(snake, 0, 0.7)
    screen.blit(snake, (75, 560))
    winScreen = Button.text(gold, (width * 0.25), (height * 0 / 12), (width * 0.5),
                            (height * 2 / 10), 150,
                            "You win!")
    winScreen.draw(screen, True)
    clock.tick(2)
    pygame.display.update()
    pygame.time.delay(4000)

def lose():
    print("You lost!")
    screen.fill((100, 100, 100))
    snake = pygame.image.load("snake5.png")
    snake.convert()
    snake = pygame.transform.rotozoom(snake, 0, 0.7)
    screen.blit(snake, (75, 560))
    gameOver = Button.text(gold, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10),
                           150,
                           "GameOver")
    gameOver.draw(screen, True)
    clock.tick(2)
    pygame.display.update()
    pygame.time.delay(4000)


def reDrawOptionsWindow():
    screen.fill(lime)
    option.draw(screen, int(theScreen.width*0.1), True)
    changeButton.draw(screen, int(theScreen.width*0.05), True)
    back_to_main.draw(screen, int(theScreen.width*0.05), True)

def options():
    reDrawOptionsWindow()
    pygame.display.update()
    opt = True
    while opt:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_to_main.isOver(pos):
                    opt = False
                if changeButton.isOver(pos):
                    questions.changeQuestionDeck("python_questions.xlsx")
            if ev.type == pygame.VIDEORESIZE:
                startWidth = ev.w
                startHeight = ev.h
                resize(startWidth, startHeight)
                reDrawOptionsWindow()

def levelChange(screen, level):
    level = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.4, theScreen.width * 0.5,
                        theScreen.height * 0.2, 200, "LEVEL " + str(level))
    screen.fill(gold)
    level.draw(screen, int(theScreen.width*0.2), True)
    pygame.display.update()
    pygame.time.delay(2000)

# enter_game = True
# while enter_game:
#     # start screen
#     menuOption = startscreen(width, height)
#
#     #  go to start, options, or quit
#     if menuOption == "start":
#         result = theBattle()
#         result = theBattle()
#     elif menuOption == "options":
#         print('this is the options')
#     elif menuOption == "quit":
#         enter_game = False
#
# pygame.quit()
def main():
    pygame.init()

    # test_sound = pygame.mixer.Sound("background_boss_music.wav")
    # pygame.mixer.Sound.play(test_sound)

    enter_game = True
    # print("dkjsflksdkjfskjlf" + str(theScreen.height))

    while enter_game:
        # start screen
        menuOption = startscreen(width, height)

        #  go to start, options, or quit
        if menuOption == "start":
            levelChange(screen, 1)
            result = theBattle()
            if result == "win":
                levelChange(screen, 2)
                result2 = theBattle()
                if result2 == "win":
                    win()
                else:
                    lose()
            else:
                lose()
        elif menuOption == "options":
            options()
        elif menuOption == "quit":
            enter_game = False
    # pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()