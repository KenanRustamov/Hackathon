import random
import math
import pygame

class Meteor():

    def __init__(self):
        self.x = random.randint(0, 400)
        self.y = -40
        self.change_x = random.randint(-5, 5)
        self.change_y = 1
        self.length = 37
        self.width = 25
        self.meteor_hit_points = [(self.x + self.width / 2, self.y + self.length), (self.x + self.width, self.y), 
        (self.x, self.y + self.length), (self.x + self.width, self.y + self.length), (self.x, self.y)]
        
    def updateMeteor(self, gameDisplay, speed, length, width, rocket, rocketValues):
        self.x += self.change_x
        self.y += self.change_y + 3*math.log10(rocket.getHeight() + 1)
        # midpoint, top right, bottom left, bottom right, top left, 
        self.meteor_hit_points = [(self.x + self.width / 2, self.y + self.length), (self.x + self.width, self.y), 
        (self.x, self.y + self.length), (self.x + self.width, self.y + self.length), (self.x, self.y)]
        for meteorHitPoint in self.meteor_hit_points:
        	pygame.draw.rect(gameDisplay, (255,0,0), pygame.Rect(meteorHitPoint[0], meteorHitPoint[1], 1, 1), 2)
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

    def collision(self, gameDisplay, rocket):

        for meteorHitPoint in self.meteor_hit_points:
            if(((((meteorHitPoint[0] - (rocket.getPos_x() + rocket.getWidth()/2 - 1))**2)/(rocket.getWidth()/2)**2) + (((meteorHitPoint[1] - (rocket.getPos_y() + rocket.getLength()/2))**2)/(rocket.getLength()/2)**2)) <= 1):
                return True

        return False

    def getX(self):
        return self.x

    #def explode(self):

    def getWidth(self):
        return self.width

    def getLength(self):
        return self.length
2
    def getY(self):
        return self.y

    