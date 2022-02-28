import pygame
import globals

pygame.init()
globals.initialize()

class Butt():
	def __init__(self, image, x, y, width_scale, height_scale):

		self.click = False
		self.image = image
		width = self.image.get_width()
		height = self.image.get_height()
		self.image = pygame.transform.scale(image, (int(width * width_scale), int(height * height_scale)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y



	def draw(self, surface):
		action = False
		if pygame.mouse.get_pressed()[0]==1:
			self.click = True
		mouse = pygame.mouse.get_pos()
		if self.rect.collidepoint(mouse):
			if self.click == True:
				globals.game_running = True
				print('cry')
		if pygame.mouse.get_pressed()[0]==0:
			self.click = False
			action = False
		surface.blit(self.image, (self.rect.x,self.rect.y))
		return action
		
