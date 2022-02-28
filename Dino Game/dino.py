import pygame
import button
import my_butt

pygame.init()

#dimensions
screen_width = 800
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height))

clock = pygame.time.Clock()
run = True
#Color
green = (0,255,0)
blue = (8,141,165)
red = (255,0,0)
bg_color = pygame.Color('grey50')

#Blank Rects
dino = pygame.Rect(600,270,50,50)
block = pygame.Rect(50,220,100,100)
play_button = pygame.Rect(400,320,300,100)

#Speed
dino_speed_x = 7
dino_speed_y = 4
block_speed_x = 3
block_speed_y = 3

#move variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False

#fonts
time_font = pygame.font.Font("fonts/Oswald-VariableFont_wght.ttf",32)
title_font = pygame.font.Font("fonts/Ubuntu-Bold.ttf", 50)

#load images
dino_img = pygame.image.load("img/icon.png").convert_alpha()
start_img = pygame.image.load("img/start_button.png").convert_alpha()
start_img.get_rect()
exit_img = pygame.image.load("img/exit_button.png").convert_alpha()

#game name
pygame.display.set_caption("dino")

#icon
pygame.display.set_icon(dino_img)

#buttons
def collision():
	if block.colliderect(dino):
		pass

	
def move():
	dino.x += dino_speed_x
	dino.y += dino_speed_y
	if moving_down:
		block.y += block_speed_y
	if moving_up:
		block.y -= block_speed_y
	if moving_right:
		block.x += block_speed_x
	if moving_left:
		block.x -= block_speed_x
def draw_bg():
	screen.fill(blue)

def draw_text(text, AA, color,x,y, font_type):
	blueprint_text = font_type.render(text, AA, color)
	screen.blit(blueprint_text, (x,y))
class menu():
	def __init__(self):
		cursor_x = 20
		cursor_y = 20
		self.cursor_rect = pygame.Rect(0,0,cursor_x,cursor_y)
		draw_text("*", True, (255,255,255), cursor_x, cursor_y, title_font)
	def draw_cursor(self):
		pass
	def draw(self):
		screen.blit(self.image, (self.rect.x,self.rect.y))


while run:
	#time
	time = pygame.time.get_ticks() 
	seconds_passed = time/1000

	#mouse pos
	mouse_pos = pygame.mouse.get_pos()

	#init methods
	draw_bg()
	move()
	collision()


	if dino.right >= screen_width or dino.x <= 0:
		dino_speed_x *= -1
	if dino.bottom >= screen_height or dino.y <= 0:
		dino_speed_y *= -1
	if block.right >= screen_width or block.x <= 0:
		moving_right = False
		moving_left = False
	if block.bottom >= screen_height or block.top <= 0:
		moving_up = False
		moving_down = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
			if event.key == pygame.K_UP:
				moving_up = True
			if event.key == pygame.K_DOWN:
				moving_down = True
			if event.key == pygame.K_LEFT:
				moving_left = True
			if event.key == pygame.K_RIGHT:
				moving_right = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				moving_up = False
			if event.key == pygame.K_DOWN:
				moving_down = False
			if event.key == pygame.K_LEFT:
				moving_left = False
			if event.key == pygame.K_RIGHT:
				moving_right = False	
		


	clock.tick(60)

	#Draw text
	draw_text("god help me", True, (255,0,0), 300,300, title_font)
	draw_text("Time:" + str(seconds_passed), True, (255,255,255), 250,250, time_font)\

	
	#Draw Rects
	pygame.draw.rect(screen, green, dino)
	pygame.draw.rect(screen, red, block)
	pygame.draw.rect(screen, bg_color, play_button)

	#update screen
	pygame.display.flip()

pygame.quit()
