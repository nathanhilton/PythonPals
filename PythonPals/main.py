import Button
import questions
import pygame
import pygame.gfxdraw
import textwrap
from player import Player, Coffee, Ruby

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class damage():
    def __init__(self, userDam, enemyDam):
        self.userDamage = userDam
        self.enemyDamage = enemyDam

    def modify(self, newUserDam, newEnemyDam):
        self.userDamage = newUserDam
        self.enemyDamage = newEnemyDam

ws = questions.initialize("python_questions.xlsx")
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

userHealth = Button.healthBar(20, 20, 200, 30, 100, "left")
enemyHealth = Button.healthBar(width - 20 - 200, 20, 200, 30, 100, "right")
title = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               "PYTHON PALS")

cat1 = Button.button(fuschia, 400, 200, 30, 30, ws['C2'].value)
cat2 = Button.button(fuschia, 650, 200, 30, 30, ws['C7'].value)
cat3 = Button.button(fuschia, 900, 200, 30, 30, ws['C12'].value)
cat4 = Button.button(fuschia, 450, 350, 30, 30, ws['C17'].value)
cat5 = Button.button(fuschia, 800, 350, 30, 30, " General")


a = Button.button(color_light, 200, 175, 25, 25)
b = Button.button(color_light, 200, 225, 25, 25)
c = Button.button(color_light, 200, 275, 25, 25)
d = Button.button(color_light, 200, 325, 25, 25)

chooseCat = Button.text(fuschia, (theScreen.width * 0.25), (theScreen.height * 0.5 / 12), (theScreen.width * 0.5),
                            (theScreen.height * 1 / 10),
                            100, "Choose a category:")

#start menu buttons
startButton = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10),
                                       "Start")
optionsButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5),
                                         (height * 2 / 10), "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Quit")
#options buttons
option = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               "OPTIONS")
chooseFighter = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10),
                                      "Choose Your Fighter")
changeButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5), (height * 2 / 10),
                                      "Change Deck")
back_to_main = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Back to Main Menu")
#choose fighter menu buttons
back_to_options = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Back to Options Menu")

damageStats = damage(50, 10)


def resize(startWidth, startHeight):
    #start menu
    title.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    startButton.modify((startWidth * 0.25), (startHeight * 3 / 12), (startWidth * 0.5),
                       (startHeight * 2 / 10))
    optionsButton.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5),
                         (startHeight * 2 / 10))
    quitButton.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                      (startHeight * 2 / 10))
    #options menu
    option.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    chooseFighter.modify((startWidth * 0.25), (startHeight * 3 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))
    changeButton.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))
    back_to_main.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))
    #choose fighter menu
    back_to_options.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))

    #category/answer buttons
    cat1.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                        (startHeight * 2 / 10))

    theScreen.width = startWidth
    theScreen.height = startHeight
    chooseCat.modify((theScreen.width * 0.25), (theScreen.height * 0 / 12), (theScreen.width * 0.5),
                     (theScreen.height * 1 / 10))

def reDrawStartWindow():
    screen.fill(gold)
    title.draw(screen, int(theScreen.width*0.1), True)
    startButton.draw(screen, int(theScreen.width*0.05), True)
    optionsButton.draw(screen, int(theScreen.width*0.05), True)
    quitButton.draw(screen, int(theScreen.width*0.05), True)

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
            if ev.type == pygame.VIDEORESIZE:
                if (ev.w != theScreen.width):
                    theScreen.width = ev.w
                    theScreen.height = int(theScreen.width * 900 / 1600)
                else:
                    theScreen.height = ev.h
                    theScreen.width = int(theScreen.height * 1600 / 900)

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resize(theScreen.width, theScreen.height)
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
                if (ev.w != theScreen.width):
                    theScreen.width = ev.w
                    theScreen.height = int(theScreen.width * 900 / 1600)
                else:
                    theScreen.height = ev.h
                    theScreen.width = int(theScreen.height * 1600 / 900)

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resizeBattle(theScreen.width, theScreen.height)
                drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height)
                drawCategories()

def resizeBattle(startWidth, startHeight):
    userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)

    a.modify(0.125 * startWidth, 0.19 * startHeight, startWidth * 0.021, startHeight * 0.021)
    b.modify(0.125 * startWidth, 0.25 * startHeight, startWidth * 0.021, startHeight * 0.021)
    c.modify(0.125 * startWidth, 0.305 * startHeight, startWidth * 0.021, startHeight * 0.021)
    d.modify(0.125 * startWidth, 0.36 * startHeight, startWidth * 0.021, startHeight * 0.021)

    chooseCat.modify(0.25 * startWidth, 1/24 * startHeight, startWidth * 0.5, startHeight * 0.1)

    cat1.modify(0.25 * startWidth, 0.22 * startHeight, startWidth * 0.025, startHeight * 0.025)
    cat2.modify(0.41 * startWidth, 0.22 * startHeight, startWidth * 0.025, startHeight * 0.025)
    cat3.modify(0.56 * startWidth, 0.22 * startHeight, startWidth * 0.025, startHeight * 0.025)
    cat4.modify(0.28 * startWidth, 0.4 * startHeight, startWidth * 0.025, startHeight * 0.025)
    cat5.modify(0.5 * startWidth, 0.4 * startHeight, startWidth * 0.025, startHeight * 0.025)

    pygame.display.update()

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
                if (ev.w != theScreen.width):
                    theScreen.width = ev.w
                    theScreen.height = int(theScreen.width * 900 / 1600)
                else:
                    theScreen.height = ev.h
                    theScreen.width = int(theScreen.height * 1600 / 900)

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resizeBattle(theScreen.width, theScreen.height)
                drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height)
                drawAnswers()

def drawBattle(playerGroup, enemyGroup, w, h):
    screen.fill(lime)
    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.1))
    bg = pygame.image.load("jungleBackground.jpg")
    bg = pygame.transform.rotozoom(bg, 0, theScreen.width/ 1380)
    screen.blit(bg,(0,0))
    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.07))
    playerGroup.draw(screen)
    enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    theScreen.width = w
    theScreen.height = h
    pygame.display.update()

#correctOrWrong is optional parameter, only use if if an animation that has has answer stuff
def drawBackground(playerGroup, enemyGroup, width, height, correctOrWrong=""):
    # pygame.display.update()
    # screen.fill(white)
    if correctOrWrong == "Correct":
        display = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.2, theScreen.width * 0.5, theScreen.height * 0.4, 100, "Correct")
    if correctOrWrong == "Wrong":
        display = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.2, theScreen.width * 0.5, theScreen.height * 0.4, 100, "Incorrect")

    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.07))
    bg = pygame.image.load("jungleBackground.jpg")
    bg = pygame.transform.rotozoom(bg, 0, theScreen.width / 1380)
    screen.blit(bg,(0,0))
    if correctOrWrong != "":
        display.draw(screen, 100, True)
    # playerGroup.draw(screen)
    # enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    # pygame.display.update()

def animationController(playerGroup, enemyGroup, width, height, clock, animation):
    if(animation == "snake attack"):
        for i in range(0,4):
            drawBackground(playerGroup, enemyGroup, width, height, "Correct")
            playerGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(5)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        playerGroup.update()

        playerGroup.update()
        playerGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()

    if(animation == "coffee hurt"):
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)

        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        
    if(animation == "coffee attack"):
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height, "Wrong")
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height, "Wrong")
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height, "Wrong")
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()

    if(animation == "snake hurt"):
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        for i in range(0, 4):
            playerGroup.update()
        playerGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        playerGroup.update()
        playerGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
    if (animation == "coffee break"):
        clock.tick(2)
        for i in range (0,6):
            playerGroup.update()
        for i in range (0,3):
            enemyGroup.update()
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(2)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(2)
    if(animation == "ruby attack"):
        for i in range(0, 7):
            drawBackground(playerGroup, enemyGroup, width, height)
            enemyGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(5)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
    if (animation == "ruby hurt"):
        for i in range(0, 7):
            enemyGroup.update()
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()

def theBattle(level):
    health = 100
    enemy_health = 100
    userHealth.set_health(health)
    enemyHealth.set_health(enemy_health)

    resizeBattle(theScreen.width, theScreen.height)

    clock = pygame.time.Clock()

    # background music
    pygame.mixer.music.load('jazz.mp3')
    pygame.mixer.music.play(-1)

    myPlayer = Player()
    playerGroup = pygame.sprite.Group(myPlayer)
    # playerGroup.draw(screen)

    if level == 1:
        myEnemy = Coffee()
    elif level == 2:
        myEnemy = Ruby()
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
        drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height)
        choose = chooseCategory(playerGroup, enemyGroup)
        print(choose)
        questionNumber = questions.load_question(choose)
        question = questions.get_question(questionNumber, ws)

        drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height)
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
            enemy_health = enemy_health - damageStats.userDamage
            enemyHealth.set_health(enemy_health)
            enemyHealth.draw(screen)

            clock.tick(5)
            animationController(playerGroup,enemyGroup,theScreen.width,theScreen.height, clock, "snake attack")
            animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock, "coffee hurt")

        else:
            health = health - damageStats.enemyDamage
            userHealth.set_health(health)
            userHealth.draw(screen)

            clock.tick(3)
            animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock, "coffee attack")
            animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock, "snake hurt")
            

        if health <= 0:
            battle = False
            return "lose"

        if enemy_health <= 0:
            battle = False
            animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock, "coffee break")
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
    winScreen.draw(screen, int(theScreen.width*0.1), True)
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
    gameOver.draw(screen, int(theScreen.width*0.1), True)
    clock.tick(2)
    pygame.display.update()
    pygame.time.delay(4000)

def reDrawOptionsWindow():
    screen.fill(lime)
    option.draw(screen, int(theScreen.width*0.1), True)
    changeButton.draw(screen, int(theScreen.width*0.05), True)
    back_to_main.draw(screen, int(theScreen.width*0.05), True)
    #chooseFighter.draw(screen, int(theScreen.width*0.05), True)
    pygame.display.update()

def options():
    reDrawOptionsWindow()
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
                    globals()['ws'] = questions.changeQuestionDeck("python_questions_capitals.xlsx", ws)
            if ev.type == pygame.VIDEORESIZE:
                if (ev.w != theScreen.width):
                    theScreen.width = ev.w
                    theScreen.height = int(theScreen.width * 900 / 1600)
                else:
                    theScreen.height = ev.h
                    theScreen.width = int(theScreen.height * 1600 / 900)

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resize(theScreen.width, theScreen.height)
                reDrawOptionsWindow()

#choose fighter functions
'''
def draw_choose_fighter_screen():
    screen.fill(lime)
    back_to_options.draw(screen, int(theScreen.width * 0.05), True)
    pygame.display.update()

def choose_your_fighter():
    draw_choose_fighter_screen()
    choice = True
    while choice:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_to_options.isOver(pos):
                    choice = False

            if ev.type == pygame.VIDEORESIZE:
                startWidth = ev.w
                startHeight = ev.h
                resize(startWidth, startHeight)
                reDrawOptionsWindow()
'''

def levelChange(screen, level, Enemy, enemyImg):
    level = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.1, theScreen.width * 0.5,
                        theScreen.height * 0.2, 200, "LEVEL " + str(level))
    enemy = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.35, theScreen.width * 0.5,
                        theScreen.height * 0.2, 100, "Your enemy is " + Enemy)
    screen.fill(gold)
    enemyimg = pygame.image.load(enemyImg)
    if Enemy == "Ruby":
        enemyimg = pygame.transform.rotozoom(enemyimg, 0, 0.68)
    else:
        print(enemy)
    level.draw(screen, int(theScreen.width*0.2), True)
    enemy.draw(screen, int(theScreen.width*0.1), True)
    screen.blit(enemyimg, (theScreen.width * 0.4, theScreen.height * 0.55))

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
    while enter_game:
        # start screen
        menuOption = startscreen()

        print(width)
        print(height)

        #  go to start, options, or quit
        if menuOption == "start":
            levelChange(screen, 1, "Java", "coffee1.png")
            #levelChange(screen, 2, "Ruby", "Ruby_idle.png")
            result = theBattle(1)
            if result == "win":
                levelChange(screen, 2, "Ruby", "Ruby_idle.png")
                damageStats.modify(25,25)
                result2 = theBattle(2)
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