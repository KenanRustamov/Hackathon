import pygame
from pygame.locals import *

pygame.font.init()
PYGBUTTON_FONT = pygame.font.Font('freesansbold.ttf', 14)

BLACK     = (  0,   0,   0)
WHITE     = (255, 255, 255)
DARKGRAY  = ( 64,  64,  64)
GRAY      = (128, 128, 128)
LIGHTGRAY = (212, 208, 200)

class PygButton():

	def __init__(self, rect=None, caption='', bgcolor=BLACK, fgcolor=LIGHTGRAY, font=None, normal=None, down=None, highlight=None):
		if rect is None:
			self._rect = pygame.Rect(20, 20, 30, 60)
		else:
			self._rect = pygame.Rect(rect)

		self._caption = caption
		self._bgcolor = bgcolor
		self._fgcolor = fgcolor

		if font is None:
			self._font = PYGBUTTON_FONT
		else:
			self._font = font

		# tracks the state of the button
		self.buttonDown = False # is the button currently pushed down?
		self.mouseOverButton = False # is the mouse currently hovering over the button?
		self.lastMouseDownOverButton = False # was the last mouse down event over the mouse button? (Used to track clicks.)
		self._visible = True # is the button visible
		self.customSurfaces = False # button starts as a text button instead of having custom images for each surface

		if normal is None:
			# create the surfaces for a text button
			self.surfaceNormal = pygame.Surface(self._rect.size)
			self.surfaceDown = pygame.Surface(self._rect.size)
			self.surfaceHighlight = pygame.Surface(self._rect.size)
			self._update() # draw the initial button images
		else:
			# create the surfaces for a custom image button
			self.setSurfaces(normal, down, highlight)

	def draw(self, surfaceObj):
		if self._visible:
			if self.buttonDown:
				surfaceObj.blit(self.surfaceDown, self._rect)
			if self.mouseOverButton:
				surfaceObj.blit(self.surfaceHighlight, self._rect)
			else:
				surfaceObj.blit(self.surfaceNormal, self._rect)

	def _update(self):
		if self.customSurfaces:
			self.surfaceNormal = pygame.transform.smoothscale(self.origSurfaceNormal, self._rect.size)
			self.surfaceDown = pygame.transform.smoothscale(self.origSurfaceDown, self._rect.size)
			self.surfaceHighlight = pygame.transform.smoothscale(self.origSurfaceHighlight, self._rect.size)
			return

		w = self._rect.width # syntactic sugar
		h = self._rect.height # syntactic sugar

		# fill background color for all buttons
		self.surfaceNormal.fill(self.bgcolor)
		self.surfaceDown.fill(self.bgcolor)
		self.surfaceHighlight.fill(self.bgcolor)

		# draw caption text for all buttons
		captionSurf = self._font.render(self._caption, True, self.fgcolor, self.bgcolor)
		captionRect = captionSurf.get_rect()
		captionRect.center = int(w / 2), int(h / 2)
		self.surfaceNormal.blit(captionSurf, captionRect)
		self.surfaceDown.blit(captionSurf, captionRect)

		# draw border for normal button
		'''pygame.draw.rect(self.surfaceNormal, BLACK, pygame.Rect((0, 0, w, h)), 1) # black border around everything
		pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (w - 2, 1))
		pygame.draw.line(self.surfaceNormal, WHITE, (1, 1), (1, h - 2))
		pygame.draw.line(self.surfaceNormal, DARKGRAY, (1, h - 1), (w - 1, h - 1))
		pygame.draw.line(self.surfaceNormal, DARKGRAY, (w - 1, 1), (w - 1, h - 1))
		pygame.draw.line(self.surfaceNormal, GRAY, (2, h - 2), (w - 2, h - 2))
		pygame.draw.line(self.surfaceNormal, GRAY, (w - 2, 2), (w - 2, h - 2))

		# draw border for down button
		pygame.draw.rect(self.surfaceDown, BLACK, pygame.Rect((0, 0, w, h)), 1) # black border around everything
		pygame.draw.line(self.surfaceDown, WHITE, (1, 1), (w - 2, 1))
		pygame.draw.line(self.surfaceDown, WHITE, (1, 1), (1, h - 2))
		pygame.draw.line(self.surfaceDown, DARKGRAY, (1, h - 2), (1, 1))
		pygame.draw.line(self.surfaceDown, DARKGRAY, (1, 1), (w - 2, 1))
		pygame.draw.line(self.surfaceDown, GRAY, (2, h - 3), (2, 2))
		pygame.draw.line(self.surfaceDown, GRAY, (2, 2), (w - 3, 2))'''

		# draw border for highlight button
		self.surfaceHighlight = self.surfaceNormal

	def handleEvent(self, eventObj):
		if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self._visible:
			return []
	
		retVal = []
	
		hasExited = False
		if not self.mouseOverButton and self._rect.collidepoint(eventObj.pos):
			self.mouseOverButton = True
			self.mouseEnter(eventObj)
			retVal.append('enter')
		elif self.mouseOverButton and not self._rect.collidepoint(eventObj.pos):
			self.mouseOverButton = False
			hasExited = True
	
		if self._rect.collidepoint(eventObj.pos):
			if eventObj.type == MOUSEMOTION:
				self.mouseMove(eventObj)
				retVal.append('move')
			elif eventObj.type == MOUSEBUTTONDOWN:
				self.buttonDown = True
				self.lastMouseDownOverButton = True
				self.mouseDown(eventObj)
				retVal.append('down')
		else:
			if eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
				self.lastMouseDownOverButton = False
	
		doMouseClick = False
		if eventObj.type == MOUSEBUTTONUP:
			if self.lastMouseDownOverButton:
				doMouseClick = True
			self.lastMouseDownOverButton = False
	
			if self.buttonDown:
				self.buttonDown = False
				self.mouseUp(eventObj)
				retVal.append('up')
	
			if doMouseClick:
				self.buttonDown = False
				self.mouseClick(eventObj)
				retVal.append('click')
	
		if hasExited:
			self.mouseExit(eventObj)
			retVal.append('exit')

		return retVal


	def mouseClick(self, event):
		self.x = 0
	def mouseEnter(self, event):
		self.fgcolor = WHITE
	def mouseExit(self, event):
		self.fgcolor = LIGHTGRAY
	def mouseMove(self, event):
		self.x = 0
	def mouseDown(self, event):
		self.x = 0
	def mouseUp(self, event):
		self.x = 0
	def setSurfaces(self, normalSurface, downSurface = None, highlightSurface = None):
		self.x = 0
	def _propGetCaption(self):
		return self._caption

	def _propSetCaption(self, captionText):
		self.customSurfaces = False
		self._caption = captionText
		self._update()

	def _propGetRect(self):
		return self._rect

	def _propSetRect(self, newRect):
		# Note that changing the attributes of the Rect won't update the button. You have to re-assign the rect member.
		self._update()
		self._rect = newRect

	def _propGetVisible(self):
		return self._visible

	def _propSetVisible(self, setting):
		self._visible = setting

	def _propGetFgColor(self):
		return self._fgcolor

	def _propSetFgColor(self, setting):
		self.customSurfaces = False
		self._fgcolor = setting
		self._update()

	def _propGetBgColor(self):
		return self._bgcolor

	def _propSetBgColor(self, setting):
		self.customSurfaces = False
		self._bgcolor = setting
		self._update()

	def _propGetFont(self):
		return self._font

	def _propSetFont(self, setting):
		self.customSurfaces = False
		self._font = setting
		self._update()

	caption = property(_propGetCaption, _propSetCaption)
	rect = property(_propGetRect, _propSetRect)
	visible = property(_propGetVisible, _propSetVisible)
	fgcolor = property(_propGetFgColor, _propSetFgColor)
	bgcolor = property(_propGetBgColor, _propSetBgColor)
	font = property(_propGetFont, _propSetFont)