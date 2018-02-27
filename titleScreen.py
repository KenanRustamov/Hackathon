from graphics import *

def title():
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
    shopMess=Text(Point(295,325),'Shop')
    shopMess.setStyle('bold')
    shopMess.setSize(24)
    shopMess.draw(win)
    titleMess=Text(Point(200,25),'League of Rockets')
    titleMess.setSize(28)
    titleMess.setStyle('bold')
    titleMess.setTextColor('white')
    titleMess.setFace('courier')
    titleMess.draw(win)
    while True:
        p=win.checkMouse()
        if p!=None:
            xval=p.getX()
            yval=p.getY()
            if (yval<375) and (yval>275):
                if (xval<190) and (xval>20):
                    return 'start'
                if (xval<380) and (xval>210):
                    return 'shop'
            
    


print(title())
