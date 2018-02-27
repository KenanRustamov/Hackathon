
class Rocket():

    def __init__(self, pos_x, pos_y, rocketWidth, rocketLength, speed = 0, steer = 2, maxFuel = 500, height = 0, weight = 10000):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.steer = steer
        self.maxFuel = maxFuel
        self.fuel = self.maxFuel
        self.height = height
        self.weight = weight
        self.width = rocketWidth
        self.length = rocketLength
        self.points = 0
        self.start_x = pos_x
        self.start_y = pos_y
        self.time = 0
        self.Vf = 300
        self.rocketWeight=11000
        self.dmdt=500
        self.hull=0
        self.acceleration= 1

    def resetRocket(self,rocketParameters):
        self.speed = 0
        self.height = 0
        self.pos_x = self.start_x
        self.pos_y = self.start_y
        self.time = 0
        self.maxFuel=rocketParameters[0]
        self.fuel = self.maxFuel
        self.dfdt=rocketParameters[1]
        self.Vf=rocketParameters[2]
        self.rocketWeight=rocketParameters[3]
        self.steer=rocketParameters[4]*2
        self.hull=rocketParameters[5]
        self.acceleration = 1

    def updateX(self, changeX):
        self.pos_x += changeX

    def updateHeight(self):
        self.points += 0.1
        self.fuel -= self.dmdt/60
        self.time += 1/60
        self.speed,self.height,self.acceleration= Rocket.physics(self.speed,self.height,self.time,self.rocketWeight,self.maxFuel,self.dmdt,self.Vf)
        if (self.speed==-10000) and (self.height==-10000):
            print("You can't take off")

    def getSteer(self):
        return self.steer

    def getPos_x(self):
        return self.pos_x

    def getPos_y(self):
        return self.pos_y

    def getSpeed(self):
        return self.speed

    def getHeight(self):
        return self.height

    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width

    def getFuel(self):
        return self.fuel

    def setHeight(self, height):
        self.height = height

    def getMaxFuel(self):
        return self.maxFuel

    def getPoints(self):
        return self.points

    def setPoints(self, money):
        self.points = money

    def addPoints(self, money):
        self.point += money

    def getAcceleration(self):
        return self.acceleration

    def getMaxVelocity(self,Mr,MfS,dmdt,vM):
        v,h,t,a,vmax,hmax,amax=0,0,0,0,0,0,0
        for i in range(10**9):
            v,h,a=Rocket.physics(v,h,t,Mr,MfS,dmdt,vM)
            t+=1/60
            if v+h==-20000:
                if (vmax <= 0):
                    raise Exception('Ship too heavy to take off. Please reconsider your life')
                return vmax
            if a>amax:
                amax=a
            if h>hmax:
                hmax=h
            if v>vmax:
                vmax=v



    def physics(v,h,t,Mr,MfS,dmdt,vM):
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
        Cd=1
        
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
            return -10000,-10000,0
        return newV,h,a