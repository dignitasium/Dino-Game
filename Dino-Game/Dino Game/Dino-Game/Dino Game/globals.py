def initialize():
	import pygame
	global screen
	screen = pygame.display.set_mode((900,506))
	global game_running
	game_running = True
	global vel
	vel = 10
	global x
	x = 0
	global moving_right
	moving_right = False
	global y
	y = 0
	global journeyman_with_gun
	