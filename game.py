from graphics import *
import pygame
import time
import Rocket
import Meteor
import SkyColor
import random
import BackgroundObject
import pygbutton
from pygame.locals import*
#gitHu
pygame.init()

def SingleColorBar(gameDisplay, color,currentFuel, maxFuel,fuelBarWidth):
    width = int(max(min(currentFuel/float(maxFuel)*fuelBarWidth, fuelBarWidth), 0))
    pygame.draw.rect(gameDisplay, color, pygame.Rect(100, 500, width, 10), 0)

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

# GLOBAL VARIABLES DO NOT TOUCH

maxVelocity = 0
maxHeight = 0
upgradeLevels=[0,0,0,0,0,0]
rocketValues=[1000,500,300,12000,1,1]
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
display_width = 400
display_height  = 600
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rockets')
rocket_width = display_width // 5
rocket_length = display_height // 6
maxHull = 1
hull = 1

img = pygame.image.load('rock2.png')
img = pygame.transform.scale(img, (rocket_width, rocket_length))
rocket_width = rocket_width* (1/3)
rocket_length = rocket_length* (3/4) + 3
meteor_img = pygame.image.load('Meteor.png')
meteor_img = pygame.transform.scale(meteor_img, (40, 40))

rocket = Rocket.Rocket(display_width/2 - rocket_width/2, display_height - (display_height / 3) - 10, rocket_width, rocket_length)
color = SkyColor.SkyColor()
FPS = 30
font = pygame.font.SysFont(None, 25)

meteors = [0, 0, 0, 0, 0]
for meteor in meteors:
    meteor = Meteor.Meteor()

backGroundObjects = [0,0,0,0,0,0,0,0,0]
for x in range(0, 9):
    backGroundObjects[x] = BackgroundObject.BackgroundObject('cloud.png', 60, 40)

pygame.font.init()
height_font = pygame.font.SysFont("Courier", 20)
text_height = height_font.render("Height: {0}".format(rocket.getHeight()),False,(0,0,0))

def resetGame(rocket):
    global maxHeight
    global maxVelocity
    maxVelocity = 0
    global blue_Shift
    global maxHull
    global hull
    hull = maxHull
    color.resetSkyColor()
    rocket.resetRocket(rocketValues)
    for x in range(0, 5):
        meteors[x] = Meteor.Meteor()

    for x in range(0, 9):
        backGroundObjects[x] = BackgroundObject.BackgroundObject('cloud.png', 60, 40)
        backGroundObjects[x].setStarBool(False)

from graphics import *

def newMainMenu():
    global rocketValues
    global upgradeLevels
    gameDisplay.fill((0, 0, 0))
    playNowButton = pygbutton.PygButton((display_width/2 - 80/2 - 10,200,100,40) , 'Play Now', black)
    shopButton = pygbutton.PygButton((display_width/2 - 80/2 - 10,240,100,40) , 'Shop', black)
    exitButton = pygbutton.PygButton((display_width/2 - 80/2 - 10,280,100,40) , 'Exit', black)
    titleFont = pygame.font.SysFont('freesansbold', 50)
    title = titleFont.render('League Of Rockets', False, (255,255,255))

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                quit()
            if 'click' in playNowButton.handleEvent(event):
                return 'start'
            if 'click' in exitButton.handleEvent(event):
                quit()
            if 'click' in shopButton.handleEvent(event):
                upgradeLevels, rocketValues, tempMoney = shop(rocket.getPoints(),upgradeLevels)
                rocket.setPoints(tempMoney)

        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(title,(50, 100))
        playNowButton.draw(gameDisplay)
        shopButton.draw(gameDisplay)
        exitButton.draw(gameDisplay)
        pygame.display.update()

'''PREVIOUS MAIN MENU METHOD
def mainMenu():
    win=GraphWin('League of Rockets', 400, 400)
    win.setBackground('black')
    bgPic=Image(Point(200,150),"myrocket.png")
    bgPic.draw(win)
    startRec=Rectangle(Point(20,275),Point(190,375))
    startRec.setFill('cyan')
    startRec.draw(win)
    shopRec=Rectangle(Point(210,275),Point(380,375))
    shopRec.setFill('red')
    shopRec.draw(win)
    startMess=Text(Point(105,325),'Take Off')
    startMess.setStyle('bold')
    startMess.setSize(24)
    startMess.draw(win)
    shopMess=Text(Point(295,325),'Quit')
    shopMess.setStyle('bold')
    shopMess.setSize(24)
    shopMess.draw(win)
    mainMenuMess=Text(Point(200,25),'League of Rockets')
    mainMenuMess.setSize(28)
    mainMenuMess.setStyle('bold')
    mainMenuMess.setTextColor('white')
    mainMenuMess.setFace('courier')
    mainMenuMess.draw(win)
    while True:
        p=win.checkMouse()
        if p!=None:
            xval=p.getX()
            yval=p.getY()
            if (yval<375) and (yval>275):
                if (xval<190) and (xval>20):
                    win.close()
                    return 'start'
                # TODO
                if (xval<380) and (xval>210):
                    win.close()
                    return 'shop'
'''
def pause():
    paused = True
    while(paused):
        #gameDisplay.fill((0,0,0))
        #myButton = customButton.customButton()
        #myButton.draw(gameDisplay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    break
            #else:
                #myButton.handleEvent(event)


def gameLoop():
    global maxVelocity
    global maxHeight
    global rocketValues
    global upgradeLevels
    global hull
    global maxHull
    global meteorDeleted
    meteorDeleted = False
    userWantsToExit = True
    starBool = False

    if newMainMenu() == 'start':
        userWantsToExit = False

    while userWantsToExit == False:

        roundOver = False
        x_change = 0
        resetGame(rocket)

        while not roundOver:

            gameDisplay.fill(color.shift(rocket.getHeight()))
            for backGroundObject in backGroundObjects:
                backGroundObject.updateBackgroundObject(rocket, display_height, display_width,gameDisplay)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change -= rocket.getSteer()
                    elif event.key == pygame.K_RIGHT:
                        x_change += rocket.getSteer()
                    elif event.key == pygame.K_ESCAPE:
                        pause()
                else:
                    x_change = 0

            if not roundOver:
                for meteor in meteors:
                    if meteor.collision(gameDisplay,rocket):
                        #pause()
                        hull = hull - 1
                        meteors.remove(meteor)
                        meteorDeleted = True
                        if hull == 0:
                        	roundOver = True
                    if meteorDeleted == True:
                    	meteors.append(Meteor.Meteor())
                    meteorDeleted = False
                    meteor.updateMeteor(gameDisplay, rocket.getSpeed(), display_height, display_width, rocket, rocketValues)
                    gameDisplay.blit(meteor_img,(meteor.getX() - 6, meteor.getY() - 2))
                    pygame.draw.rect(gameDisplay, (255,0,0), pygame.Rect(meteor.getX(), meteor.getY(), meteor.getWidth(), meteor.getLength()), 2)


            if (rocket.getPos_x() + x_change) < display_width - rocket_width and (rocket.getPos_x() + x_change) > 0:
                rocket.updateX(x_change)
            gameDisplay.blit(img,(rocket.getPos_x() - 26, rocket.getPos_y() - 3))

            rocket.updateHeight()
            currentVelocity = rocket.getSpeed()
            if(currentVelocity > maxVelocity):
                maxVelocity = currentVelocity

            currentHeight = rocket.getHeight()
            if(currentHeight > maxHeight):
                maxHeight = currentHeight

            pygame.draw.ellipse(gameDisplay, (0,0,0), (rocket.getPos_x(), rocket.getPos_y(), rocket.getWidth(), rocket.getLength()), 2)

            if (currentVelocity <= 0):
                roundOver = True
                resetGame(rocket) 
                break
                
            if rocket.getFuel() > 0:
                fuelBarColor = (255 - int(rocket.getFuel()/rocket.getMaxFuel()*255), int(rocket.getFuel()/rocket.getMaxFuel()*255), 0)
            else:
                fuelBarColor = red
            pygame.draw.rect(gameDisplay, black, pygame.Rect(100, 500, 200, 10), 2)
            SingleColorBar(gameDisplay, fuelBarColor, rocket.getFuel(), rocket.getMaxFuel(), 200)
            myfont = pygame.font.SysFont('Comic Sans', 25)
            velocity = myfont.render('Curret Velocity : '  + str(int(currentVelocity)) + ' m/s', False, (255,0,0))
            acceleration = myfont.render('Curret Acceleration : '  + str(int(rocket.getAcceleration())) + ' m/s\u00b2', False, (255,0,0))
            height = myfont.render('Curret Height : '  + str(int(currentHeight)) + ' m', False, (255,0,0))
            gameDisplay.blit(height,(display_width/2 - 80, 520))
            gameDisplay.blit(velocity,(display_width / 2 - 85,540))
            gameDisplay.blit(acceleration,(display_width / 2 - 110,560))
            pygame.display.update()

            text_height = height_font.render('Height: {0}'.format(currentHeight),False,(0,0,0))
            gameDisplay.blit(text_height, (0,0))

            clock.tick(FPS)
        descision = newGameOverScreen(maxHeight, maxVelocity)
        if(descision == 'Main Menu'):
            newMainMenu()
        if(descision == 'Shop'):
            print('shop')
            upgradeLevels, rocketValues, tempMoney = shop(rocket.getPoints(),upgradeLevels)
            rocket.setPoints(tempMoney)
        resetGame(rocket)
        print("GAME OVER")
    userWantsToExit = True

# GAME OVER

def newGameOverScreen(maxH, maxV):
    global rocketValues
    global upgradeLevels
    gameDisplay.fill(pygame.Color("black"))
    mainMenuButton = pygbutton.PygButton((40,display_height - 40,100,40) , 'Main Menu', black)
    shopButton = pygbutton.PygButton((display_width - 120,display_height - 40,100,40) , 'Shop', black)
    titleFont = pygame.font.SysFont('freesansbold', 50)
    title = titleFont.render('Game Over!', False, (255,255,255))
    statisticsFont = pygame.font.SysFont('freesansbold', 25)
    maxHeightText = statisticsFont.render('Highest Height Reached: ' + str(int(maxH)) + ' m', False, (255,255,255))
    maxVelocityText = statisticsFont.render('Highest Speed Reached: ' + str(int(maxV)) + 'm/s' , False, (255,255,255))

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                quit()
            if 'click' in mainMenuButton.handleEvent(event):
                return 'Main Menu'
            if 'click' in shopButton.handleEvent(event):
                return 'Shop'
        gameDisplay.fill((0, 0, 0))
        gameDisplay.blit(title,((display_width/2 - 200/2), 100))
        gameDisplay.blit(maxHeightText,((display_width/2 - 110, 275)))
        gameDisplay.blit(maxVelocityText,((display_width/2 - 110, 325)))
        mainMenuButton.draw(gameDisplay)
        shopButton.draw(gameDisplay)
        pygame.display.update()


def gameOverScreen():
    global rocketValues
    global upgradeLevels
    running = True
    gameDisplay.fill(pygame.Color("white"))
    myfont = pygame.font.SysFont('Comic Sans', 50)
    textSurface = myfont.render('Round Over!', False, (0,0,0))
    otherFont = pygame.font.SysFont('Comic Sans', 25)
    mainMenuSurface = otherFont.render('Main Menu', False, (0,0,0))
    shopSurface = otherFont.render('Shop', False, (0,0,0))
    mainMenuButton = pygame.Rect(75, 200, 100, 40)
    shopButton = pygame.Rect(225, 200, 100, 40)
    #GitHub Test

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if mainMenuButton.collidepoint(mouse_pos):
                    mainMenu()

                if shopButton.collidepoint(mouse_pos):
                    upgradeLevels, rocketValues, tempMoney = shop(rocket.getPoints(),upgradeLevels)
                    rocket.setPoints(tempMoney)
                    return None

        gameDisplay.blit(textSurface, (100, 100))
        pygame.draw.rect(gameDisplay, [255, 0, 0], mainMenuButton)
        pygame.draw.rect(gameDisplay, [255, 0, 0], shopButton)
        gameDisplay.blit(mainMenuSurface, (80, 210))
        gameDisplay.blit(shopSurface, (255, 210))
        pygame.display.update()

def shop(money, currentUpgrades):
    money = 10**5
    massDecreaseList=[10000,7500,5000,2500,1000,0]
    massFuelList=[1000,2000,4000,8000,16000,32000]
    massHull=[1000,2000,3000,4000,5000,6000]
    fuelEjectSpeed=[500,750,1000,1500,2000,3000]
    fuelVelocity=[300,600,900,1200,1500,1800]
    m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
    win=GraphWin('Shop',800,500)
    rocketBg=Rectangle(Point(0,100),Point(250,500))
    rocketBg.setFill('grey')
    rocketBg.setOutline('grey')
    rocketBg.draw(win)
    rocket=Image(Point(125,300),"Rocket.bmp")
    rocket.draw(win)
    statsBox=Rectangle(Point(250,0),Point(850,175))
    statsBox.setOutline('grey')
    statsBox.setFill('grey')
    statsBox.draw(win)
    buyBox=Rectangle(Point(250,175),Point(850,500))
    buyBox.setFill('grey')
    buyBox.setOutline('grey')
    buyBox.draw(win)
    goAgainBox=Rectangle(Point(0,0),Point(250,100))
    goAgainBox.setFill('green')
    goAgainBox.setOutline('green')
    goAgainBox.draw(win)
    goAgainQuestion=Text(Point(125,50),'Go Fly')
    goAgainQuestion.setFace('courier')
    goAgainQuestion.setSize(36)
    goAgainQuestion.setStyle('bold')
    goAgainQuestion.draw(win)
    currentStatsHeader=Text(Point(400,25),'Current Stats')
    currentStatsHeader.setSize(20)
    currentStatsHeader.setFace('courier')
    currentStatsHeader.draw(win)
    moneyLine=Text(Point(650,25),['Money:','$',"%.2f" %money])
    moneyLine.setSize(20)
    moneyLine.setFace('courier')
    moneyLine.draw(win)
    currentFuel=Text(Point(400,75),['Fuel','Mass:',massFuelList[currentUpgrades[0]],'kg'])
    currentFuel.setSize(14)
    currentFuel.setFace('courier')
    currentFuel.draw(win)
    fuelPerS=Text(Point(650,75),['Fuel/s:',fuelEjectSpeed[currentUpgrades[1]],'kg/s'])
    fuelPerS.setSize(14)
    fuelPerS.setFace('courier')
    fuelPerS.draw(win)
    fuelV=Text(Point(400,100),['Fuel','Velocity:',fuelVelocity[currentUpgrades[2]],'m/s'])
    fuelV.setSize(14)
    fuelV.setFace('courier')
    fuelV.draw(win)
    currentMass=Text(Point(650,100),['Mass:',m,'kg'])
    currentMass.setSize(14)
    currentMass.setFace('courier')
    currentMass.draw(win)
    currentSteering=Text(Point(400,125),['Handling:','lvl',currentUpgrades[4]+1])
    currentSteering.setSize(14)
    currentSteering.setFace('courier')
    currentSteering.draw(win)
    currentHull=Text(Point(650,125),['Hull:','lvl',currentUpgrades[5]+1])
    currentHull.setSize(14)
    currentHull.setFace('courier')
    currentHull.draw(win)
    global maxHull
    for i in range(2):
        for j in range(3):
            button=Rectangle(Point(290+260*i,200+100*j),Point(515+260*i,275+100*j))
            button.setFill('orange')
            button.draw(win)
    strLis=[['Upgrade Fuel Amount','Upgrade Vf','Upgrade Steering'],['Upgrade Fuel/s','Lower Mass','Upgrade Hull']]
    for i in range(2):
        for j in range(3):
            mess=Text(Point(402+260*i,225+100*j),strLis[i][j])
            mess.setSize(14)
            mess.setFace('courier')
            mess.draw(win)
    priceList=[10,25,50,100,200]
    priceTextList=[]
    for i in range(2):
        for j in range(3):
            if currentUpgrades[2*j+i]==5:
                 mess=Text(Point(402+260*i,250+100*j),'Sold Out')
            else:
                mess=Text(Point(402+260*i,250+100*j),['$',priceList[currentUpgrades[2*j+i]]])
            mess.setSize(14)
            mess.setFace('courier')
            mess.draw(win)
            priceTextList.append(mess)
    while True:
        p=win.checkMouse()

        if p!=None:
            xval=p.getX()
            yval=p.getY()
            if (xval<250) and (yval<100):
                win.close()
                valLis=[massFuelList[currentUpgrades[0]],fuelEjectSpeed[currentUpgrades[1]],fuelVelocity[currentUpgrades[2]],m,currentUpgrades[4]+1,currentUpgrades[5]+1]
                return currentUpgrades,valLis,money
            if (xval>290) and (xval<515):
                if (yval>200) and (yval<275):
                    if currentUpgrades[0]<4:
                        if money>=priceList[currentUpgrades[0]]:
                            money+=-priceList[currentUpgrades[0]]
                            currentUpgrades[0]+=1
                            currentFuel.setText(['Fuel','Mass:',massFuelList[currentUpgrades[0]],'kg'])
                            priceTextList[0].setText(['$',priceList[currentUpgrades[0]]])
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[0]==4:
                        if money>=priceList[currentUpgrades[0]]:
                            money+=-priceList[currentUpgrades[0]]
                            currentUpgrades[0]+=1
                            currentFuel.setText(['Fuel','Mass:',massFuelList[currentUpgrades[0]],'kg'])
                            priceTextList[0].setText('Sold out')
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>300) and (yval<375):
                    if currentUpgrades[2]<4:
                        if money>=priceList[currentUpgrades[2]]:
                            money+=-priceList[currentUpgrades[2]]
                            currentUpgrades[2]+=1
                            fuelV.setText(['Fuel','Velocity:',fuelVelocity[currentUpgrades[2]],'m/s'])
                            priceTextList[1].setText(['$',priceList[currentUpgrades[2]]])
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[2]==4:
                        if money>=priceList[currentUpgrades[2]]:
                            money+=-priceList[currentUpgrades[2]]
                            currentUpgrades[2]+=1
                            fuelV.setText(['Fuel','Velocity:',fuelVelocity[currentUpgrades[2]],'m/s'])
                            priceTextList[1].setText('Sold out')
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>400) and (yval<475):
                    if currentUpgrades[4]<4:
                        if money>=priceList[currentUpgrades[4]]:
                            money+=-priceList[currentUpgrades[4]]
                            currentUpgrades[4]+=1
                            currentSteering.setText(['Handling:','lvl',currentUpgrades[4]+1])
                            priceTextList[2].setText(['$',priceList[currentUpgrades[4]]])
                            moneyLine.setText(['Money:','$',"%2.f"%money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[4]==4:
                        if money>=priceList[currentUpgrades[4]]:
                            money+=-priceList[currentUpgrades[4]]
                            currentUpgrades[4]+=1
                            currentSteering.setText(['Handling:','lvl',currentUpgrades[4]+1])
                            priceTextList[2].setText('Sold out')
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
            if (xval>550) and (xval<775):
                if (yval>200) and (yval<275):
                    if currentUpgrades[1]<4:
                        if money>=priceList[currentUpgrades[1]]:
                            money+=-priceList[currentUpgrades[1]]
                            currentUpgrades[1]+=1
                            fuelPerS.setText(['Fuel/s:',fuelEjectSpeed[currentUpgrades[1]],'kg/s'])
                            priceTextList[3].setText(['$',priceList[currentUpgrades[1]]])
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[1]==4:
                        if money>=priceList[currentUpgrades[1]]:
                            money+=-priceList[currentUpgrades[1]]
                            currentUpgrades[1]+=1
                            fuelPerS.setText(['Fuel/s:',fuelEjectSpeed[currentUpgrades[1]],'kg/s'])
                            priceTextList[3].setText('Sold out')
                            moneyLine.setText(['Money:','$',"%.2f" % money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>300) and (yval<375):
                    if currentUpgrades[3]<4:
                        if money>=priceList[currentUpgrades[3]]:
                            money+=-priceList[currentUpgrades[3]]
                            currentUpgrades[3]+=1
                            currentMass.setText(['Mass:',m,'kg'])
                            priceTextList[4].setText(['$',priceList[currentUpgrades[3]]])
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[3]==4:
                        if money>=priceList[currentUpgrades[3]]:
                            money+=-priceList[currentUpgrades[3]]
                            currentUpgrades[3]+=1
                            currentMass.setText(['Mass:',m,'kg'])
                            priceTextList[4].setText('Sold out')
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>400) and (yval<475):
                    if currentUpgrades[5]<4:
                        if money>=priceList[currentUpgrades[5]]:
                            money+=-priceList[currentUpgrades[5]]
                            currentUpgrades[5]+=1
                            currentHull.setText(['Hull:','lvl',currentUpgrades[5]+1])
                            priceTextList[5].setText(['$',priceList[currentUpgrades[5]]])
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            maxHull = maxHull + 1
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[5]==4:
                        if money>=priceList[currentUpgrades[5]]:
                            money+=-priceList[currentUpgrades[5]]
                            currentUpgrades[5]+=1
                            currentHull.setText(['Hull:','lvl',currentUpgrades[5]+1])
                            priceTextList[5].setText('Sold out')
                            moneyLine.setText(['Money:','$',"%.2f" %money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])

gameLoop()