import random
import math


class Meteor():

    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = -40
        self.change_x = random.randint(-5, 5)
        self.change_y = 1
        self.length = 40
        self.width = 40
        
    def updateMeteor(self, speed, length, width, rocket, rocketValues):
        self.x += self.change_x
        self.y += self.change_y + 3*math.log10(rocket.getHeight() + 1)
        if (self.y >= length or self.x >= width or self.x <= 0):
            Meteor.__init__(self)

    def isInsideRocket(rocket, coords):
        if (coords[0] >= rocket.getPos_x() and coords[0] <= rocket.getPos_x() + rocket.getWidth() and
            coords[1] >= rocket.getPos_y() and coords[1] <= rocket.getPos_y() + rocket.getLength()):
                return True
        return False

#Collision detection algorithim changed
    def rectangularCollision(self, rocket):
        meteor_hit_points = [(self.x, self.y), (self.x + self.width, self.y), 
            (self.x, self.y + self.length), (self.x + self.width, self.y + self.length),
            (self.x + self.width / 2, self.y + self.length)]
        for point in meteor_hit_points:
            if (Meteor.isInsideRocket(rocket, point)):
                return True

        return False

    def collision(self, rocket):
        meteor_hit_points = [(self.x + self.width / 2, self.y + self.length), (self.x + self.width, self.y), 
            (self.x, self.y + self.length), (self.x + self.width, self.y + self.length), (self.x, self.y)]
        for meteorHitPoint in meteor_hit_points:
            if(((((meteorHitPoint[0] - (rocket.getPos_x() + rocket.getWidth()/2 - 1))**2)/(rocket.getWidth()/2)**2) + (((meteorHitPoint[1] - (rocket.getPos_y() + rocket.getLength()/2))**2)/(rocket.getLength()/2)**2)) <= 1):
                return True

        return False

    def getX(self):
        return self.x

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length

    def getY(self):
        return self.y

    