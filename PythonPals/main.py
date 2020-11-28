from Button import button
import questions
import pygame
import pygame.gfxdraw
import textwrap
from player import Player, Coffee, Ruby, Eye

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

# class level():
#     def __init__(self, level):
#         self.level = level


ws = questions.initialize("python_questions.xlsx")
screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
white = (255, 255, 255)
purple = (110, 113, 198)
blue = (64, 127, 194)
indigo = (51, 57, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
fuschia = (255, 0, 255)
black = (0, 0, 0)
gold = (197, 179, 88)
lime = (153, 255, 51)
width = screen.get_width()
height = screen.get_height()
#screen.fill(lime)

clock = pygame.time.Clock()

theScreen = Screen(screen.get_width(), screen.get_height())

userHealth = Button.healthBar(20, 20, 200, 30, 100, "left")
enemyHealth = Button.healthBar(width - 20 - 200, 20, 200, 30, 100, "right")
damageStats = damage(50, 10)

cat1 = Button.button(fuschia, 400, 200, 30, 30, " " + ws['C2'].value)
cat2 = Button.button(fuschia, 650, 200, 30, 30, " " + ws['C7'].value)
cat3 = Button.button(fuschia, 900, 200, 30, 30, " " + ws['C12'].value)
cat4 = Button.button(fuschia, 450, 350, 30, 30, " " + ws['C17'].value)
cat5 = Button.button(fuschia, 800, 350, 30, 30, "General")

a = Button.button(color_light, 200, 175, 25, 25)
b = Button.button(color_light, 200, 225, 25, 25)
c = Button.button(color_light, 200, 275, 25, 25)
d = Button.button(color_light, 200, 325, 25, 25)

chooseCat = Button.text(fuschia, (theScreen.width * 0.25), (theScreen.height * 0.5 / 12), (theScreen.width * 0.5),
                            (theScreen.height * 1 / 10),
                            100, ["Choose a category:"])

#start menu buttons
title = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                    ["PYTHON PALS"])
startButton = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10),
                                       "Start")
optionsButton = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5), (height * 2 / 10),
                              "Options")
quitButton = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Quit")
#options menu buttons
optionsHeader = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               ["OPTIONS"])
choose_q_deck = Button.button(color_light, (width * 0.25), (height * 3 / 12), (width * 0.5), (height * 2 / 10),
                                      "Choose Question Deck")
change_sound_settings = Button.button(color_light, (width * 0.25), (height * 6 / 12), (width * 0.5), (height * 2 / 10),
                                      "Change Sound Settings")
back_to_main = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Back to Main Menu")

#options -> return to options
back_to_options = Button.button(color_light, (width * 0.25), (height * 9 / 12), (width * 0.5), (height * 2 / 10),
                                      "Back to Options Menu")

#options -> choose question deck
q_deck_header = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               ["QUESTION DECKS"])
changeCapitals = Button.button(color_light, (width * 0.25), (height * 3 / 14), (width * 0.5), (height * 2 / 14),
                                      "Use Capitals Deck")
changePython = Button.button(color_light, (width * 0.25), (height * 6 / 14), (width * 0.5), (height * 2 / 14),
                                      "Use Python Deck")
changeHistory = Button.button(color_light, (width * 0.25), (height * 9 / 14), (width * 0.5), (height * 2 / 14),
                                      "Use History Deck")

#options -> change sound settings
sound_header = Button.text(black, (width * 0.25), (height * 0 / 12), (width * 0.5), (height * 2 / 10), 150,
                               ["SOUND SETTINGS"])


def resize(startWidth, startHeight):
    # battle scene
    cat1 = Button.button(fuschia, 400, 200, 30, 30, " " + ws['C2'].value)
    cat2 = Button.button(fuschia, 650, 200, 30, 30, " " + ws['C7'].value)
    cat3 = Button.button(fuschia, 900, 200, 30, 30, " " + ws['C12'].value)
    cat4 = Button.button(fuschia, 450, 350, 30, 30, " " + ws['C17'].value)
    cat5 = Button.button(fuschia, 800, 350, 30, 30, " General")

    # category/answer buttons
    cat1.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5),
                (startHeight * 2 / 10))

    #start menu
    title.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    startButton.modify((startWidth * 0.25), (startHeight * 3 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    optionsButton.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    quitButton.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5), (startHeight * 2 / 10))

    #options menu
    optionsHeader.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    choose_q_deck.modify((startWidth * 0.25), (startHeight * 3 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    change_sound_settings.modify((startWidth * 0.25), (startHeight * 6 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    back_to_main.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5), (startHeight * 2 / 10))

    #options -> submenus
    back_to_options.modify((startWidth * 0.25), (startHeight * 9 / 12), (startWidth * 0.5), (startHeight * 2 / 10))

    #options -> choose question deck menu
    q_deck_header.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))
    changeCapitals.modify((startWidth * 0.25), (startHeight * 3 / 14), (startWidth * 0.5), (startHeight * 2 / 14))
    changePython.modify((startWidth * 0.25), (startHeight * 5.5 / 14), (startWidth * 0.5), (startHeight * 2 / 14))
    changeHistory.modify((startWidth * 0.25), (startHeight * 8 / 14), (startWidth * 0.5), (startHeight * 2 / 14))

    #options -> change sound settings menu
    sound_header.modify((startWidth * 0.25), (startHeight * 0 / 12), (startWidth * 0.5), (startHeight * 2 / 10))

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
                # not sure what the commented part is?

                # if (ev.w != theScreen.width):
                #     theScreen.width = ev.w
                #     theScreen.height = int(theScreen.width * 900 / 1600)
                # else:
                #     theScreen.height = ev.h
                #     theScreen.width = int(theScreen.height * 1600 / 900)
                theScreen.width = ev.w
                theScreen.height = ev.h

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
    cat1 = Button.button(fuschia, 400, 200, 30, 30, " " + ws['C2'].value)
    cat2 = Button.button(fuschia, 650, 200, 30, 30, " " + ws['C7'].value)
    cat3 = Button.button(fuschia, 900, 200, 30, 30, " " + ws['C12'].value)
    cat4 = Button.button(fuschia, 450, 350, 30, 30, " " + ws['C17'].value)
    cat5 = Button.button(fuschia, 800, 350, 30, 30, " General")

    chooseCat.draw(screen, int(theScreen.width * 0.07), True)
    cat1.draw(screen, int(theScreen.width * 0.02))
    cat2.draw(screen, int(theScreen.width * 0.02))
    cat3.draw(screen, int(theScreen.width * 0.02))
    cat4.draw(screen, int(theScreen.width * 0.02))
    cat5.draw(screen, int(theScreen.width * 0.02))

def chooseCategory(playerGroup, enemyGroup,level):
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
                # not sure what the commented part is?

                # if (ev.w != theScreen.width):
                #     theScreen.width = ev.w
                #     theScreen.height = int(theScreen.width * 900 / 1600)
                # else:
                #     theScreen.height = ev.h
                #     theScreen.width = int(theScreen.height * 1600 / 900)
                theScreen.width = ev.w
                theScreen.height = ev.h

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resizeBattle(theScreen.width, theScreen.height)
                drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height,level)
                drawCategories()

def resizeBattle(startWidth, startHeight):
    userHealth.modify(0.02 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)
    enemyHealth.modify(0.88 * startWidth, 0.02 * startHeight, startWidth * 0.1, startHeight * 0.03)

    a.modify(0.125 * startWidth, 0.19 * startHeight, startWidth * 0.021, startHeight * 0.021)
    b.modify(0.125 * startWidth, 0.25 * startHeight, startWidth * 0.021, startHeight * 0.021)
    c.modify(0.125 * startWidth, 0.305 * startHeight, startWidth * 0.021, startHeight * 0.021)
    d.modify(0.125 * startWidth, 0.36 * startHeight, startWidth * 0.021, startHeight * 0.021)

    chooseCat.modify(0.25 * startWidth, 1/24 * startHeight, startWidth * 0.5, startHeight * 0.1)
    cat1 = Button.button(fuschia, 400, 200, 30, 30, " " + ws['C2'].value)
    cat2 = Button.button(fuschia, 650, 200, 30, 30, " " + ws['C7'].value)
    cat3 = Button.button(fuschia, 900, 200, 30, 30, " " + ws['C12'].value)
    cat4 = Button.button(fuschia, 450, 350, 30, 30, " " + ws['C17'].value)
    cat5 = Button.button(fuschia, 800, 350, 30, 30, " General")

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

def chooseAnswer(playerGroup, enemyGroup, question,level,q,A,B,C,D):
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
                # not sure what the commented part is?

                # if (ev.w != theScreen.width):
                #     theScreen.width = ev.w
                #     theScreen.height = int(theScreen.width * 900 / 1600)
                # else:
                #     theScreen.height = ev.h
                #     theScreen.width = int(theScreen.height * 1600 / 900)
                theScreen.width = ev.w
                theScreen.height = ev.h

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resizeBattle(theScreen.width, theScreen.height)
                drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height,level)
                q.draw(screen, int(theScreen.width * 0.02), False)
                q.draw(screen, int(theScreen.width * 0.02), False)
                A.draw(screen, int(theScreen.width * 0.015), False)
                B.draw(screen, int(theScreen.width * 0.015), False)
                C.draw(screen, int(theScreen.width * 0.015), False)
                D.draw(screen, int(theScreen.width * 0.015), False)
                drawAnswers()

def drawBattle(playerGroup, enemyGroup, w, h,level):
    screen.fill((0,0,0))
    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.1))
    # bg = pygame.image.load("jungleBackground.jpg")
    drawBackground(playerGroup,enemyGroup,w,h,level)
    # bg = pygame.transform.rotozoom(bg, 0, theScreen.width/ 1380)
    # screen.blit(bg,(0,0))
    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.07))
    playerGroup.draw(screen)
    enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    theScreen.width = w
    theScreen.height = h
    pygame.display.update()

#correctOrWrong is optional parameter, only use if if an animation that has has answer stuff
def drawBackground(playerGroup, enemyGroup, width, height,level, correctOrWrong=""):
    # pygame.display.update()
    # screen.fill(white)
    #pygame.draw.rect(screen, (0, 0, 0), (0, 0, theScreen.width, theScreen.height * 0.07))
    if level == 1:
        bg = pygame.image.load("jungleBackground.jpg")
        bg = pygame.transform.rotozoom(bg, 0, theScreen.width / 1380)
    elif level == 2:
        bg = pygame.image.load("treasure.jpg")
        bg = pygame.transform.rotozoom(bg, 0, theScreen.width / 1920)
    else:
        bg = pygame.image.load("lava.png")
        bg = pygame.transform.rotozoom(bg, 0, theScreen.height / 727)
    screen.blit(bg,(0,0))
    if correctOrWrong != "":
        if correctOrWrong == "Correct":
            display = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.2, theScreen.width * 0.5,
                                  theScreen.height * 0.4, 100, ["Correct"])
            pygame.draw.rect(screen, (0,255,0), (theScreen.width * 0.35, theScreen.height * 0.3, theScreen.width * 0.3, theScreen.height * 0.2))
        if correctOrWrong == "Wrong":
            display = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.2, theScreen.width * 0.5,
                                  theScreen.height * 0.4, 100, ["Incorrect"])
            pygame.draw.rect(screen, (255, 0, 0), (theScreen.width * 0.35, theScreen.height * 0.3, theScreen.width * 0.3, theScreen.height * 0.2))
        display.draw(screen, 100, True)
    # playerGroup.draw(screen)
    # enemyGroup.draw(screen)
    enemyHealth.draw(screen)
    userHealth.draw(screen)
    # pygame.display.update()

def animationController(playerGroup, enemyGroup, width, height, clock, level, animation):
    if(animation == "snake attack"):
        for i in range(0,4):
            drawBackground(playerGroup, enemyGroup, width, height,level, "Correct")
            playerGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(5)
        drawBackground(playerGroup, enemyGroup, width, height,level, "Correct")
        playerGroup.update()

        playerGroup.update()
        playerGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()

    if(animation == "coffee hurt"):
        drawBackground(playerGroup, enemyGroup, width, height,level, "Correct")
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)

        drawBackground(playerGroup, enemyGroup, width, height,level, "Correct")
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        
    if(animation == "coffee attack"):
        drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()

    if(animation == "snake hurt"):
        drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
        for i in range(0, 4):
            playerGroup.update()
        playerGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
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
        drawBackground(playerGroup, enemyGroup, width, height,level)
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(2)
        drawBackground(playerGroup, enemyGroup, width, height,level)
        enemyGroup.update()
        enemyGroup.draw(screen)
        playerGroup.draw(screen)
        pygame.display.update()
        clock.tick(2)
    if(animation == "ruby attack"):
        for i in range(0, 7):
            drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
            enemyGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(5)
        drawBackground(playerGroup, enemyGroup, width, height,level, "Wrong")
        enemyGroup.update()
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
    if (animation == "ruby hurt"):
        for i in range(0, 7):
            enemyGroup.update()
        drawBackground(playerGroup, enemyGroup, width, height,level, "Correct")
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, width, height,level, "Correct")
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
    if (animation == "eye attack"):
        for i in range(0, 2):
            drawBackground(playerGroup, enemyGroup, width, height, level, "Wrong")
            enemyGroup.update()
            playerGroup.draw(screen)
            enemyGroup.draw(screen)
            pygame.display.update()
            clock.tick(2)
        drawBackground(playerGroup, enemyGroup, width, height, level, "Wrong")
        enemyGroup.update()
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
    if (animation == "eye hurt"):
        for i in range(0, 2):
            enemyGroup.update()
        drawBackground(playerGroup, enemyGroup, width, height, level, "Correct")
        enemyGroup.update()
        playerGroup.draw(screen)
        enemyGroup.draw(screen)
        pygame.display.update()
        clock.tick(3)
        drawBackground(playerGroup, enemyGroup, width, height, level, "Correct")
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
    #pygame.mixer.music.load('funke.mp3')
    #pygame.mixer.music.play(-1)

    myPlayer = Player()
    playerGroup = pygame.sprite.Group(myPlayer)
    # playerGroup.draw(screen)

    if level == 1:
        myEnemy = Coffee()
        pygame.mixer.music.load('jazz.mp3')
        pygame.mixer.music.play(-1)
    elif level == 2:
        myEnemy = Ruby()
        pygame.mixer.music.load('funke.mp3')
        pygame.mixer.music.play(-1)
    else:
        myEnemy = Eye()
        pygame.mixer.music.load('bluth.wav')
        pygame.mixer.music.play(-1)
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
        drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height,level)
        choose = chooseCategory(playerGroup, enemyGroup,level)
        print(choose)
        questionNumber = questions.load_question(choose)
        question = questions.get_question(questionNumber, ws)

        drawBattle(playerGroup, enemyGroup, theScreen.width, theScreen.height,level)

        q = Button.text(black, 400, 100, 50, 50, 40, question[0].splitlines())
        pygame.gfxdraw.box(screen, pygame.Rect(0, theScreen.height * 0.1, theScreen.width, 75),
                           (77, 153, 83, 130))
        A = Button.text(black, a.x, a.y, 50, 50, 40, question[1].splitlines())
        B = Button.text(black, b.x, b.y, 50, 50, 40, question[2].splitlines())
        C = Button.text(black, c.x, c.y, 50, 50, 40, question[3].splitlines())
        D = Button.text(black, d.x, d.y, 50, 50, 40, question[4].splitlines())
        pygame.gfxdraw.box(screen, pygame.Rect(theScreen.width * 0.1, theScreen.height * 0.15,
                                               600, 300), (77, 153, 83, 130))
        q.draw(screen, int(theScreen.width*0.02), False)
        A.draw(screen, int(theScreen.width*0.015), False)
        B.draw(screen, int(theScreen.width*0.015), False)
        C.draw(screen, int(theScreen.width*0.015), False)
        D.draw(screen, int(theScreen.width*0.015), False)

        guess = chooseAnswer(playerGroup, enemyGroup, question,level,q,A,B,C,D)
        is_correct = questions.get_result(guess, question[5])

        if is_correct:
            enemy_health = enemy_health - damageStats.userDamage
            enemyHealth.set_health(enemy_health)
            enemyHealth.draw(screen)

            clock.tick(5)
            animationController(playerGroup,enemyGroup,theScreen.width,theScreen.height, clock,level, "snake attack")
            if level == 1:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock,level, "coffee hurt")
            elif level == 2:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock,level, "ruby hurt")
            else:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock, level, "eye hurt")


        else:
            health = health - damageStats.enemyDamage
            userHealth.set_health(health)
            userHealth.draw(screen)

            clock.tick(3)
            if level == 1:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock,level, "coffee attack")
            elif level == 2:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock,level, "ruby attack")
            else:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock, level, "eye attack")
            animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock,level, "snake hurt")
            

        if health <= 0:
            battle = False
            return "lose"

        if enemy_health <= 0:
            battle = False
            if level == 1:
                animationController(playerGroup, enemyGroup, theScreen.width, theScreen.height, clock,level, "coffee break")

            return "win"

def win():
    pygame.mixer.music.load('victoire.mp3')
    pygame.mixer.music.play(-1)

    print("You won!")
    screen.fill((100, 100, 100))
    snake = pygame.image.load("snake6.png")
    snake.convert()
    # snake = pygame.transform.rotozoom(snake, 0, 0.7)
    screen.blit(snake, (theScreen.width * 0.43, theScreen.height * 0.6))
    winScreen = Button.text(gold, (theScreen.width * 0.25), (theScreen.height * 0 / 12), (theScreen.width * 0.5),
                            (theScreen.height * 2 / 10), 150,
                            ["You win!"])
    winScreen.draw(screen, int(theScreen.width*0.1), True)
    clock.tick(2)
    pygame.display.update()
    pygame.time.delay(4000)

def lose():
    pygame.mixer.music.load('defaite.mp3')
    pygame.mixer.music.play(-1)

    print("You lost!")
    screen.fill((100, 100, 100))
    snake = pygame.image.load("snake5.png")
    snake.convert()
    #snake = pygame.transform.rotozoom(snake, 0, 0.7)
    screen.blit(snake, (theScreen.width * 0.4, theScreen.height * 0.6))
    gameOver = Button.text(gold, (theScreen.width * 0.25), (theScreen.height * 0 / 12), (theScreen.width * 0.5), (theScreen.height * 2 / 10),
                           150,
                           ["GameOver"])
    gameOver.draw(screen, int(theScreen.width*0.1), True)
    clock.tick(2)
    pygame.display.update()
    pygame.time.delay(4000)

def reDrawOptionsWindow():
    screen.fill(purple)
    optionsHeader.draw(screen, int(theScreen.width*0.1), True)
    choose_q_deck.draw(screen, int(theScreen.width*0.05), True)
    change_sound_settings.draw(screen, int(theScreen.width*0.05), True)
    back_to_main.draw(screen, int(theScreen.width*0.05), True)
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
                if choose_q_deck.isOver(pos):
                    q_deck_menu()
                    opt = False
                    break
                if change_sound_settings.isOver(pos):
                    sound_settings_menu()
                    opt = False
                    break
            if ev.type == pygame.VIDEORESIZE:
                theScreen.width = ev.w
                theScreen.height = ev.h

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resize(theScreen.width, theScreen.height)
                reDrawOptionsWindow()

#options -> choose question deck
def redraw_q_deck_window():
    screen.fill(blue)
    q_deck_header.draw(screen, int(theScreen.width*0.1), True)
    changeCapitals.draw(screen, int(theScreen.width*0.05), True)
    changePython.draw(screen, int(theScreen.width*0.05), True)
    changeHistory.draw(screen, int(theScreen.width*0.05), True)
    back_to_options.draw(screen, int(theScreen.width*0.05), True)
    pygame.display.update()

def q_deck_menu():
    redraw_q_deck_window()
    opt = True
    while opt:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_to_options.isOver(pos):
                    options()
                    opt = False
                if changeCapitals.isOver(pos):
                    globals()['ws'] = questions.changeQuestionDeck("python_questions_capitals.xlsx", ws)
                    options()
                    opt = False
                if changePython.isOver(pos):
                    globals()['ws'] = questions.changeQuestionDeck("python_questions.xlsx", ws)
                    options()
                    opt = False
                if changeHistory.isOver(pos):
                    globals()['ws'] = questions.changeQuestionDeck("python_questions_timeline.xlsx", ws)
                    options()
                    opt = False
            if ev.type == pygame.VIDEORESIZE:
                theScreen.width = ev.w
                theScreen.height = ev.h

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resize(theScreen.width, theScreen.height)
                redraw_q_deck_window()

#options -> change sound settings
def redraw_sound_window():
    screen.fill(blue)
    sound_header.draw(screen, int(theScreen.width*0.1), True)
    back_to_options.draw(screen, int(theScreen.width*0.05), True)
    pygame.display.update()

def sound_settings_menu():
    redraw_sound_window()
    opt = True
    while opt:
        for ev in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if ev.type == pygame.QUIT:
                pygame.quit()
                quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if back_to_options.isOver(pos):
                    options()
                    opt = False
            if ev.type == pygame.VIDEORESIZE:
                theScreen.width = ev.w
                theScreen.height = ev.h

                pygame.display.set_mode((theScreen.width, theScreen.height), pygame.RESIZABLE)
                resize(theScreen.width, theScreen.height)
                redraw_sound_window()


def levelChange(screen, level, Enemy, enemyImg):
    level = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.1, theScreen.width * 0.5,
                        theScreen.height * 0.2, 200, ["LEVEL " + str(level)])
    enemy = Button.text(black, theScreen.width * 0.25, theScreen.height * 0.35, theScreen.width * 0.5,
                        theScreen.height * 0.2, 100, ["Your enemy is " + Enemy])
    screen.fill(gold)
    enemyimg = pygame.image.load(enemyImg)
    if Enemy == "Ruby":
        enemyimg = pygame.transform.rotozoom(enemyimg, 0, 0.68)
    elif Enemy == "Eye":
        enemyimg = pygame.transform.rotozoom(enemyimg, 0, 0.85)

    level.draw(screen, int(theScreen.width*0.2), True)
    enemy.draw(screen, int(theScreen.width*0.1), True)
    if Enemy != "Eye":
        screen.blit(enemyimg, (theScreen.width * 0.4, theScreen.height * 0.55))
    else:
        screen.blit(enemyimg, (theScreen.width * 0.35, theScreen.height * 0.55))

    pygame.display.update()
    pygame.time.delay(2000)

def main():

    pygame.init()

    pygame.display.set_caption("Python Pals")

    enter_game = True
    while enter_game:
        pygame.mixer.music.load('idle.wav')
        pygame.mixer.music.play(-1)

        # start screen
        menuOption = startscreen()

        print(width)
        print(height)

        #  go to start, options, or quit
        if menuOption == "start":
            damageStats.modify(50,10)
            levelChange(screen, 1, "Java", "coffee1.png")
            result = theBattle(1)
            if result == "win":
                levelChange(screen, 2, "Ruby", "Ruby_idle.png")
                damageStats.modify(25,25)
                result2 = theBattle(2)
                if result2 == "win":
                    levelChange(screen, 3, "Eye", "C1.png")
                    damageStats.modify(17,25)
                    result3 = theBattle(3)
                    if result3 == "win":
                        win()
                    else:
                        lose()
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