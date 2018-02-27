
import Rocket

class Color():

    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b
    
    def shift(self, speed):
        self.r -= speed
        self.g -= speed
        self.b -= speed
        return (r, g, b)