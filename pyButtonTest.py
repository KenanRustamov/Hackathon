import sys, os
sys.path.insert(0, os.path.abspath('..'))

import pygame, pygbutton
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 380
WINDOWHEIGHT = 350

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

def play():
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	gameDisplay = pygame.display.set_mode((400,400))
	pygame.display.set_caption('pyButtonTest')
	gameDisplay.fill((0, 0, 0))
	myButton = pygbutton.PygButton((50,50,80,20) , 'buttonTest', BLACK)

	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				quit()
			for text in myButton.handleEvent(event):
				print(text)
			if (event.type == pygame.KEYDOWN):
				if event.type == pygame.K_ESCAPE:
					running = False
					break

		gameDisplay.fill((0, 0, 0))
		myButton.draw(gameDisplay)
		pygame.display.update()
		FPSCLOCK.tick(FPS)


play()