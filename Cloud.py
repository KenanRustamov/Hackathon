import random
import pygame

class Cloud():

    def __init__(self, imageInput, xSize, ySize):
        self.image = pygame.image.load(imageInput)
        self.image = pygame.transform.scale(self.image, (random.randint(xSize-xSize/10,xSize + xSize/10), random.randint(xSize - xSize/10,xSize - xSize/10)))
        self.x = random.randint(10, 390)
        self.y = random.randint(0,600)
        self.change_x = 0
        self.change_y = 1
        self.starBool = False
        
    def updateCloud(self, rocket, height, width, display):
        self.y += self.change_y + (rocket.getSpeed() / 10)
        display.blit(self.image,(self.x, self.y))
        if (self.y >= height or self.x >= width or self.x <= 0):
            if(rocket.getHeight() > 10000 and self.starBool != True):
                Cloud.setImage(self, 'star.png', 20, 20) 
                self.starBool = True
            self.y = -40
            self.change_x = 0
            self.change_y = 1

    def getImage(self):
        return self.image

    def setStarBool(self, isLoaded):
        self.starBool = isLoaded


    def setImage(self, newImageInput, xSize, ySize):
        self.image = pygame.image.load(newImageInput)
        self.image = pygame.transform.scale(self.image, (random.randint(xSize-xSize/10,xSize + xSize/10), random.randint(xSize - xSize/10,xSize - xSize/10)))

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    