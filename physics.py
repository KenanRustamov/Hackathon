import time
from graphics import *

def wait(t):
    val=time.time()
    while time.time()-t<val:
        pass
    return None

def rocket(v,h,t,Mr=100000,MfS=5000000,dmdt=500000,vM=1000,Cd=1):
    #earth constants
    Re=6371000
    Me=5.972*10**24
    G=6.67408*10**-11

    #air density
    exponent=G*Me*.0289644/(8.3144*.0064)
    p=1.225-.00004083*h
    if p<0:
        p=0
        
    #drag values
    A=10
    
    #fuel values
    Mf=MfS-t*dmdt
    if Mf<0:
        Mf=0
        dmdt=0

    #gravity and mass
    g=G*Me/(Re+h)**2
    currentM=Mr+Mf

    #acceleration and velocity
    if v>0:
        a=(vM*(dmdt)-currentM*g-1/2*1*p*v**2*A*Cd)/currentM
    else:
        a=(vM*(dmdt)-currentM*g+1/2*1*p*v**2*A*Cd)/currentM
    newV=v+a/60
    h+=newV/60
    if h<=0:
        print('rip ship')
        return -1,-1,-1,-1
    return a,newV,h,Mf

def getMaxs(Mr,Mf,dmdt,vM):
    v,h,a,vmax,hmax,amax=0,0,0,0,0,0
    massFuel=Mf
    for i in range(100000):
        a,v,h,massFuel=rocket(v,h,i/60,Mr,Mf,dmdt,vM)
        if (a==-1) and (v==-1) and (h==-1) and (massFuel==-1):
            return hmax,vmax,amax
        if a>amax:
            amax=a
        if v>vmax:
            vmax=v
        if h>hmax:
            hmax=h
        

def flyRocket(Mr,Mf,dmdt,vM):
    recL=[]
    v=0
    h=0
    a=0
    win=GraphWin('Rocet Test',1000,500)
    for i in range(10):
        
        rec=Rectangle(Point(40+100*i,480),Point(60+100*i,500))
        rec.setFill('red')
        line=Line(Point(100*i,0),Point(100*i,500))
        line.draw(win)
        rec.draw(win)
        recL.append(rec)
    Hmess=Text(Point(75,25),'hold')
    Hmess.draw(win)
    Vmess=Text(Point(75,50),'hold')
    Vmess.draw(win)
    Amess=Text(Point(75,75),'hold')
    Amess.draw(win)
    Tmess=Text(Point(75,100),'hold')
    Tmess.draw(win)
    Mmess=Text(Point(75,125),'hold')
    Mmess.draw(win)
    
    
    change=0
    massFuel=Mf
    for i in range(100000):
        Hmess.setText(['h=','%.2f'%h,'m'])
        Vmess.setText(['v=','%.2f'%v,'m/s'])
        Amess.setText(['a=','%.2f'%a,'m/s^2'])
        Tmess.setText(['t=','%.2f'%(i/60),'s'])
        Mmess.setText(['m=','%.2f'%(massFuel+Mr),'kg'])
        a,v,h,massFuel=rocket(v,h,i/60,Mr,Mf,dmdt,vM)
        if a+v+h+massFuel==-4:
            return 'rip ship'
        if change==0:
            if massFuel==False:
                for i in range(10):
                    recL[i].setFill('blue')
                change=1
        for i in range(10):
            recL[i].move(0,-v/(10**i))
        wait(1/60)
    
print(getMaxs(11000,1000,500,1800))

print(flyRocket(6000,32000,3000,1800))
