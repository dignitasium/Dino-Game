import pygame
from pygame.locals import *
import globals

pygame.init()
globals.initialize()

def main_menu():
	flip = False
	while True:
		userInput = pygame.key.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		globals.screen.fill((168,59,21))
		
		#background
		bg = pygame.image.load('img/r.jpg').convert_alpha()
		globals.screen.blit(bg, (0,0))
		
		#start
		start_img = pygame.image.load('img/start_button.png').convert_alpha()
		globals.screen.blit(start_img,(180,100))
		start_rect = start_img.get_rect()
		start_rect.x = 180
		start_rect.y = 100
		
		#player
		journeyman_with_gun = pygame.image.load('img/journeyman_with_gun.png').convert_alpha()
		if flip:
			pygame.transform.flip(journeyman_with_gun, True, False)
		globals.screen.blit(journeyman_with_gun, (globals.x,globals.y))
		
		#settings
		settings_img = pygame.image.load('img/settings.png').convert_alpha()
		settings_img = pygame.transform.scale(settings_img, (350,150))
		settings_rect = settings_img.get_rect()
		settings_rect.x = 260
		settings_rect.y = 250
		globals.screen.blit(settings_img, (260,250))

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()		
			if userInput[K_d]:
				globals.x += globals.vel
				flip = False
			if userInput[K_s]:
				globals.y += globals.vel				
			if userInput[K_a]:
				globals.x -= globals.vel
				flip = True
			if userInput[K_w]:
				globals.y -= globals.vel
		if start_rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed(3)[2] == 1:
				play()
		if settings_rect.collidepoint(mouse_pos):
			if pygame.mouse.get_pressed(3)[2] == 1:
				settings()

		pygame.display.update()
		clock = pygame.time.Clock()
		clock.tick(60)

def settings():
	running_settings = True
	while running_settings:
		globals.screen.fill((0,0,0))
		font = pygame.font.SysFont(None, 15)
		play = font.render('settings', True, (255,255,255))
		globals.screen.blit(play, (250,200))
		clock = pygame.time.Clock()
		clock.tick(60)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running_settings = False


def play():
	running_play = True
	while running_play:
		globals.screen.fill((0,0,0))
		font = pygame.font.SysFont(None, 15)
		play = font.render('play', True, (255,255,255))
		globals.screen.blit(play, (250,200))
		clock = pygame.time.Clock()
		clock.tick(60)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running_play = False

main_menu()