import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SHIP_WIDTH = 49
SHIP_HEIGHT = 45

def main():
	# initialize pygame
	pygame.init()
	#pygame.mixer.init()

	# set caption
	pygame.display.set_caption("pygame basic setup")

	# set up clock object
	clock = pygame.time.Clock()
	FPS = 60

	# set up screen object
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	background = pygame.image.load("background2.png")


	# SHIP INFORMATION
	my_ship = pygame.image.load("ship2.png")
	ship_x = 0.5 * SCREEN_WIDTH - 0.5 * SHIP_WIDTH
	ship_y = SCREEN_HEIGHT - SHIP_HEIGHT
	sx_change = 0
	sy_change = 0
	loaded = True # flag to determine if you can shoot again yet

	# MISSLE 1 INFORMATION
	missle = pygame.image.load("missle.png")
	mx = ship_x
	my = ship_y
	mx_change = 0
	my_change = 0
	loaded = True

	# MISSLE 2 INFORMATION
	missle2 = pygame.image.load("missle2.png")
	mx2 = ship_x - 5
	my2 = ship_y
	mx2_change = 0
	my2_change = 0

	# Sound effects
	shoot = pygame.mixer.Sound("shoot.wav")
	pygame.mixer.music.load("space_music.mp3")
	pygame.mixer.music.play(-1, 0.0)


	# game loop
	running = True
	while running:

		# event handling loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					sx_change -= 5
				if event.key == pygame.K_RIGHT:
					sx_change += 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					sx_change = 0
				if event.key == pygame.K_RIGHT:
					sx_change = 0
				if event.key == pygame.K_SPACE:
					if loaded:
						#mx = ship_x
						#mx2 = ship_x + SHIP_WIDTH - 10
						my_change = -20
						my2_change = -20
						shoot.play()
					loaded = False
		if ship_x + sx_change < 0:
			sx_change = 0
		if ship_x + sx_change > SCREEN_WIDTH - SHIP_WIDTH:
			sx_change = 0

		ship_x += sx_change

		screen.blit(background, (0, 0))
		screen.blit(my_ship, (ship_x, ship_y))

		if not loaded:
			if my <= 0:
				mx = ship_x
				my = ship_y
				mx2 = ship_x + SHIP_WIDTH
				my2 = ship_y
				loaded = True
			else:
				screen.blit(missle, (mx, my))
				screen.blit(missle2, (mx2, my2))
				my += my_change
				my2 += my2_change
		pygame.display.flip()
		clock.tick(FPS)

if __name__ == "__main__":
	main()