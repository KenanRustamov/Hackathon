from graphics import *

def shop(money, currentUpgrades):
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
    rocket=Image(Point(125,300),"rocket.png")
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
    moneyLine=Text(Point(650,25),['Money:','$',money])
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
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[0]==4:
                        if money>=priceList[currentUpgrades[0]]:
                            money+=-priceList[currentUpgrades[0]]
                            currentUpgrades[0]+=1
                            currentFuel.setText(['Fuel','Mass:',massFuelList[currentUpgrades[0]],'kg'])
                            priceTextList[0].setText('Sold out')
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>300) and (yval<375):
                    if currentUpgrades[2]<4:
                        if money>=priceList[currentUpgrades[2]]:
                            money+=-priceList[currentUpgrades[2]]
                            currentUpgrades[2]+=1
                            fuelV.setText(['Fuel','Velocity:',fuelVelocity[currentUpgrades[2]],'m/s'])
                            priceTextList[1].setText(['$',priceList[currentUpgrades[2]]])
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[2]==4:
                        if money>=priceList[currentUpgrades[2]]:
                            money+=-priceList[currentUpgrades[2]]
                            currentUpgrades[2]+=1
                            fuelV.setText(['Fuel','Velocity:',fuelVelocity[currentUpgrades[2]],'m/s'])
                            priceTextList[1].setText('Sold out')
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>400) and (yval<475):
                    if currentUpgrades[4]<4:
                        if money>=priceList[currentUpgrades[4]]:
                            money+=-priceList[currentUpgrades[4]]
                            currentUpgrades[4]+=1
                            currentSteering.setText(['Handling:','lvl',currentUpgrades[4]+1])
                            priceTextList[2].setText(['$',priceList[currentUpgrades[4]]])
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[4]==4:
                        if money>=priceList[currentUpgrades[4]]:
                            money+=-priceList[currentUpgrades[4]]
                            currentUpgrades[4]+=1
                            currentSteering.setText(['Handling:','lvl',currentUpgrades[4]+1])
                            priceTextList[2].setText('Sold out')
                            moneyLine.setText(['Money:','$',money])
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
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[1]==4:
                        if money>=priceList[currentUpgrades[1]]:
                            money+=-priceList[currentUpgrades[1]]
                            currentUpgrades[1]+=1
                            fuelPerS.setText(['Fuel/s:',fuelEjectSpeed[currentUpgrades[1]],'kg/s'])
                            priceTextList[3].setText('Sold out')
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>300) and (yval<375):
                    if currentUpgrades[3]<4:
                        if money>=priceList[currentUpgrades[3]]:
                            money+=-priceList[currentUpgrades[3]]
                            currentUpgrades[3]+=1
                            currentMass.setText(['Mass:',m,'kg'])
                            priceTextList[4].setText(['$',priceList[currentUpgrades[3]]])
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[3]==4:
                        if money>=priceList[currentUpgrades[3]]:
                            money+=-priceList[currentUpgrades[3]]
                            currentUpgrades[3]+=1
                            currentMass.setText(['Mass:',m,'kg'])
                            priceTextList[4].setText('Sold out')
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                if (yval>400) and (yval<475):
                    if currentUpgrades[5]<4:
                        if money>=priceList[currentUpgrades[5]]:
                            money+=-priceList[currentUpgrades[5]]
                            currentUpgrades[5]+=1
                            currentHull.setText(['Hull:','lvl',currentUpgrades[5]+1])
                            priceTextList[5].setText(['$',priceList[currentUpgrades[5]]])
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                    elif currentUpgrades[5]==4:
                        if money>=priceList[currentUpgrades[5]]:
                            money+=-priceList[currentUpgrades[5]]
                            currentUpgrades[5]+=1
                            currentHull.setText(['Hull:','lvl',currentUpgrades[5]+1])
                            priceTextList[5].setText('Sold out')
                            moneyLine.setText(['Money:','$',money])
                            m=massDecreaseList[currentUpgrades[3]]+massFuelList[currentUpgrades[0]]+massHull[currentUpgrades[5]]
                            currentMass.setText(['Mass:',m,'kg'])
                        
    
print(shop(10**8,[0,0,0,0,0,0]))
